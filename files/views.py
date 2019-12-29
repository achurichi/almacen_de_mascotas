from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.db.models import Q
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .models import PetFile, Owner
from .forms import PetForm, OwnerForm


def petFiles_list(request):
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


def pet_file_detail(request, pk):
    petFile = get_object_or_404(PetFile, pk=pk)
    petForm = PetForm(instance=petFile)
    ownerForm = OwnerForm(instance=petFile.owner)
    context = {
        'petFile': petFile,
        'ownerFile': petFile.owner,
        'petForm': petForm,
        'ownerForm': ownerForm,
    }
    return render(request, 'files/pet_file_detail.html', context)


def delete_file(request):
    pet_id = request.POST.get('pet_id', None)
    owner_id = PetFile.objects.filter(id=pet_id)[0].owner.pk
    PetFile.objects.filter(id=pet_id).delete()
    # Si el dueño no tiene mas animales también debe eliminarse
    if len(PetFile.objects.filter(owner_id=owner_id)) == 0:
        Owner.objects.filter(id=owner_id).delete()

    return JsonResponse({'pet_id': pet_id})


def add_pet(request):
    newOwner = None
    if request.method == "POST" or request.method == "FILES":
        petForm = PetForm(request.POST, request.FILES)
        ownerForm = OwnerForm(request.POST)
        newOwner = request.POST.get('owner_option', None)
    else:
        petForm = PetForm(initial={'sex': 'Macho'})
        ownerForm = OwnerForm()

    if petForm.is_valid() and newOwner == "True":
        savedOwner = ownerForm.save()
        petForm = petForm.save(commit=False)
        petForm.owner = savedOwner
        petForm.save()
        return HttpResponseRedirect(reverse('files:pets_list'))
    elif petForm.is_valid() and newOwner == "False":
        owner_id = request.POST.get('owner_id', None)
        if owner_id != "":
            existingOwner = Owner.objects.filter(id=owner_id)
            petForm = petForm.save(commit=False)
            petForm.owner = existingOwner[0]
            petForm.save()
            return HttpResponseRedirect(reverse('files:pets_list'))

    context = {
        'petForm': petForm,
        'ownerForm': ownerForm,
    }
    return render(request, 'files/add_pet.html', context)


def search_owners(request):
    search_text = request.GET.get('search_text', None)
    existingOwners = Owner.objects.filter(
        owner_name__contains=search_text)[0:40]
    data = dict()

    for i, owner in enumerate(existingOwners):
        data["owner"+str(i)] = {
            'owner_name': owner.owner_name,
            'address': owner.address,
            'phone_number_1': owner.phone_number_1,
            'phone_number_2': owner.phone_number_2,
            'phone_number_3': owner.phone_number_3,
            'id': owner.id,
        }

    return JsonResponse(data)
