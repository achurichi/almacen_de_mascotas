from django.core.paginator import Paginator
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

    petFiles = PetFile.objects.filter(
        Q(pet_name__icontains=query)).distinct().order_by('-created_at')
    paginator = Paginator(petFiles, 6)
    page = request.GET.get('page')
    petFiles = paginator.get_page(page)

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
        petFiles = PetFile.objects.filter(Q(pet_name__icontains=q)).distinct()

        for petFile in petFiles:
            queryset.append(petFile)
    return list(set(queryset))


def delete_file(request):
    pet_id = request.POST.get('pet_id', None)
    owner_id = PetFile.objects.filter(id=pet_id)[0].owner.pk
    PetFile.objects.filter(id=pet_id).delete()
    # Si el dueño no tiene mas animales también debe eliminarse
    if len(PetFile.objects.filter(owner_id=owner_id)) == 0:
        Owner.objects.filter(id=owner_id).delete()

    return JsonResponse({'pet_id': pet_id})


def pet_show_info(request, pk):
    petFile = get_object_or_404(PetFile, pk=pk)
    petForm = PetForm(instance=petFile)
    ownerForm = OwnerForm(instance=petFile.owner)
    context = {
        'petFile': petFile,
        'ownerFile': petFile.owner,
    }
    return render(request, 'files/pet_show_info.html', context)


def pet_edit_info(request, pk):
    if request.method == "POST":
        pet_id = request.POST.get('pet_id', None)
        petFile = get_object_or_404(PetFile, id=pet_id)
        petForm = PetForm(request.POST, request.FILES, instance=petFile)
        if petForm.has_changed() and petForm.is_valid():
            petForm.save()

        owner_id = request.POST.get('owner_id', None)
        owner = get_object_or_404(Owner, id=owner_id)
        ownerForm = OwnerForm(request.POST, instance=owner)
        if ownerForm.has_changed() and ownerForm.is_valid():
            ownerForm.save()

        url = reverse('files:show_info', kwargs={'pk': pet_id})
        return HttpResponseRedirect(url)

    petFile = get_object_or_404(PetFile, pk=pk)
    petForm = PetForm(instance=petFile)
    ownerForm = OwnerForm(instance=petFile.owner)
    context = {
        'petFile': petFile,
        'ownerFile': petFile.owner,
        'petForm': petForm,
        'ownerForm': ownerForm,
    }
    return render(request, 'files/pet_edit_info.html', context)


def pet_show_clinic_history(request, pk):
    petFile = get_object_or_404(PetFile, pk=pk)
    petForm = PetForm(instance=petFile)
    context = {
        'petFile': petFile,
    }
    return render(request, 'files/pet_show_clinic_history.html', context)


def pet_show_vaccination_history(request, pk):
    petFile = get_object_or_404(PetFile, pk=pk)
    petForm = PetForm(instance=petFile)
    context = {
        'petFile': petFile,
    }
    return render(request, 'files/pet_show_vaccination_history.html', context)


def pet_show_deworming_history(request, pk):
    petFile = get_object_or_404(PetFile, pk=pk)
    petForm = PetForm(instance=petFile)
    context = {
        'petFile': petFile,
    }
    return render(request, 'files/pet_show_deworming_history.html', context)


def pet_show_internment_history(request, pk):
    petFile = get_object_or_404(PetFile, pk=pk)
    petForm = PetForm(instance=petFile)
    context = {
        'petFile': petFile,
    }
    return render(request, 'files/pet_show_internment_history.html', context)


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
