from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q

from .models import PetFile, Owner
from .forms import PetForm, OwnerForm


def petFiles_list(request):
    # petFiles = PetFile.objects.all()
    query = ""
    if request.GET:
        query = request.GET['q']

    petFiles = petFiles_list_queryset(query)

    context = {
        'query': str(query),
        'petFiles': petFiles,
    }

    return render(request, 'files/pet_files_list.html', context)


def petFiles_list_queryset(query=None):
    """Función para obtener una lista con las fichas filtradas"""
    queryset = []
    queries = query.split(" ")
    for q in queries:
        petFiles = PetFile.objects.filter(
            Q(pet_name__icontains=q) |
            Q(id__icontains=q)
        ).distinct()

        for petFile in petFiles:
            queryset.append(petFile)
    return list(set(queryset))


def add_pet(request):
    petForm = PetForm(request.POST or None)
    ownerForm = OwnerForm(request.POST or None)
    if petForm.is_valid() and ownerForm.is_valid():
        savedPetFile = petForm.save()
        ownerForm = ownerForm.save(commit=False)
        ownerForm.petFile = savedPetFile
        ownerForm.save()
        # petForm = PetForm()
        # ownerForm = OwnerForm()

        return petFiles_list(request)

    context = {
        'petForm': petForm,
        'ownerForm': ownerForm,
    }
    return render(request, 'files/add_pet.html', context)
