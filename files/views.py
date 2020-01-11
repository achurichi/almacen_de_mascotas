import datetime
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.db.models import Q
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.forms import modelformset_factory

from .models import PetFile, Owner, ClinicHistory, ClinicHistoryImg, VaccinationHistory, DewormingHistory
from .forms import PetForm, OwnerForm, ClinicHistoryForm, ClinicHistoryImgForm, VaccinationHistoryForm, DewormingHistoryForm


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

    return JsonResponse({})


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


def pet_show_info(request, pk):
    petFile = get_object_or_404(PetFile, pk=pk)
    context = {
        'petFile': petFile,
        'ownerFile': petFile.owner,
    }
    return render(request, 'files/pet_show_info.html', context)


def pet_edit_info(request, pk):
    if request.method == "POST":
        petFile = get_object_or_404(PetFile, id=pk)
        petForm = PetForm(request.POST, request.FILES, instance=petFile)
        if petForm.has_changed() and petForm.is_valid():
            petForm.save()

        owner_id = PetFile.objects.filter(id=pk)[0].owner.pk
        owner = get_object_or_404(Owner, id=owner_id)
        ownerForm = OwnerForm(request.POST, instance=owner)
        if ownerForm.has_changed() and ownerForm.is_valid():
            ownerForm.save()

        url = reverse('files:show_info', kwargs={'pk': pk})
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


def clinic_history_list(request, pk):
    petFile = get_object_or_404(PetFile, pk=pk)
    clinicHistory_files = ClinicHistory.objects.filter(
        petFile=pk).order_by('-date')

    paginator = Paginator(clinicHistory_files, 10)
    page = request.GET.get('page')
    clinicHistory_files = paginator.get_page(page)

    context = {
        'petFile': petFile,
        'clinicHistory_files': clinicHistory_files,
    }
    return render(request, 'files/clinic_history_list.html', context)


def delete_clinic_history(request):
    clinicHistory_id = request.POST.get('clinicHistory_id', None)
    ClinicHistory.objects.filter(id=clinicHistory_id).delete()
    return JsonResponse({})


def new_clinic_history(request, pk):
    petFile = get_object_or_404(PetFile, pk=pk)
    ImgFormset = modelformset_factory(ClinicHistoryImg,
                                      form=ClinicHistoryImgForm,
                                      extra=1,)

    if request.method == "POST":
        clinicHistoryForm = ClinicHistoryForm(request.POST)
        imgFormset = ImgFormset(request.POST,
                                request.FILES,
                                queryset=ClinicHistoryImg.objects.none())

        if clinicHistoryForm.is_valid():
            clinicHistoryForm = clinicHistoryForm.save(commit=False)
            clinicHistoryForm.petFile = petFile
            if clinicHistoryForm.date == None:
                clinicHistoryForm.date = datetime.date.today()
            clinicHistoryForm.save()

            if request.FILES != {} and imgFormset.is_valid():
                for form in imgFormset.cleaned_data:
                    if form != {}:
                        photo = ClinicHistoryImg(
                            clinicHistory=clinicHistoryForm, image=form['image'])
                        photo.save()

            url = reverse('files:clinic_history_list', kwargs={'pk': pk})
            return HttpResponseRedirect(url)
    else:
        clinicHistoryForm = ClinicHistoryForm()
        imgFormset = ImgFormset(queryset=ClinicHistoryImg.objects.none())

    context = {
        'petFile': petFile,
        'clinicHistoryForm': clinicHistoryForm,
        'imgFormset': imgFormset,
    }

    return render(request, 'files/new_clinic_history.html', context)


def show_clinic_history(request, pk, clinic_history_pk):
    petFile = get_object_or_404(PetFile, pk=pk)
    clinicHistory = get_object_or_404(ClinicHistory, pk=clinic_history_pk)
    clinicHistoryImg = ClinicHistoryImg.objects.filter(
        clinicHistory=clinicHistory)
    context = {
        'petFile': petFile,
        'clinicHistory': clinicHistory,
        'clinicHistoryImg': clinicHistoryImg,
    }
    return render(request, 'files/show_clinic_history.html', context)


def edit_clinic_history(request, pk, clinic_history_pk):
    ImgFormset = modelformset_factory(ClinicHistoryImg,
                                      form=ClinicHistoryImgForm,
                                      extra=1,
                                      can_delete=True,)

    if request.method == "POST":
        clinicHistory = get_object_or_404(ClinicHistory, pk=clinic_history_pk)
        clinicHistoryForm = ClinicHistoryForm(
            request.POST, instance=clinicHistory)
        imgFormset = ImgFormset(request.POST,
                                request.FILES,
                                queryset=ClinicHistoryImg.objects.filter(
                                    clinicHistory_id=clinic_history_pk))
        if clinicHistoryForm.has_changed() and clinicHistoryForm.is_valid():
            if clinicHistory.date == None:
                clinicHistory.date = datetime.date.today()
            clinicHistoryForm.save()

        if imgFormset.is_valid():
            for form in imgFormset.cleaned_data:
                print(form)
                if form == {} or form['id'] == None and form['DELETE'] == True:
                    break
                else:
                    if form['id'] == None:
                        photo = ClinicHistoryImg(
                            clinicHistory=clinicHistory, image=form['image'])
                        photo.save()
                    elif form['DELETE'] == True:
                        ClinicHistoryImg.objects.filter(
                            id=form['id'].pk).delete()
                    else:
                        photo = ClinicHistoryImg.objects.filter(
                            id=form['id'].pk)[0]
                        if photo.image != form['image']:
                            photo.image = form['image']
                            photo.save()

        url = reverse('files:show_clinic_history', kwargs={
                      'pk': pk, 'clinic_history_pk': clinic_history_pk})
        return HttpResponseRedirect(url)

    petFile = get_object_or_404(PetFile, pk=pk)
    clinicHistory = get_object_or_404(ClinicHistory, pk=clinic_history_pk)
    clinicHistoryForm = ClinicHistoryForm(instance=clinicHistory)
    imgFormset = ImgFormset(queryset=ClinicHistoryImg.objects.filter(
        clinicHistory_id=clinic_history_pk))

    context = {
        'petFile': petFile,
        'clinicHistory': clinicHistory,
        'clinicHistoryForm': clinicHistoryForm,
        'imgFormset': imgFormset,
    }

    return render(request, 'files/edit_clinic_history.html', context)


def vaccination_history_list(request, pk):
    petFile = get_object_or_404(PetFile, pk=pk)

    if request.method == "POST":
        vaccinationForm = VaccinationHistoryForm(request.POST)
        if vaccinationForm.is_valid():
            vaccinationForm = vaccinationForm.save(commit=False)
            vaccinationForm.petFile = petFile
            vaccinationForm.save()

            url = reverse('files:vaccination_history_list', kwargs={'pk': pk})
            return HttpResponseRedirect(url)

    vaccinationHistory_list = VaccinationHistory.objects.filter(
        petFile=pk).order_by('-date')
    vaccinationForm = VaccinationHistoryForm()

    paginator = Paginator(vaccinationHistory_list, 10)
    page = request.GET.get('page')
    vaccinationHistory_list = paginator.get_page(page)

    context = {
        'petFile': petFile,
        'vaccinationHistory_list': vaccinationHistory_list,
        'vaccinationForm': vaccinationForm,
    }

    return render(request, 'files/vaccination_history_list.html', context)


def delete_vaccination_history(request):
    vaccinationHistory_id = request.POST.get('vaccinationHistory_id', None)
    VaccinationHistory.objects.filter(id=vaccinationHistory_id).delete()
    return JsonResponse({})


def deworming_history_list(request, pk):
    petFile = get_object_or_404(PetFile, pk=pk)

    if request.method == "POST":
        dewormingForm = DewormingHistoryForm(request.POST)
        if dewormingForm.is_valid():
            dewormingForm = dewormingForm.save(commit=False)
            dewormingForm.petFile = petFile
            dewormingForm.save()

            url = reverse('files:deworming_history_list', kwargs={'pk': pk})
            return HttpResponseRedirect(url)

    dewormingHistory_list = DewormingHistory.objects.filter(
        petFile=pk).order_by('-date')
    dewormingForm = DewormingHistoryForm()

    paginator = Paginator(dewormingHistory_list, 10)
    page = request.GET.get('page')
    dewormingHistory_list = paginator.get_page(page)

    context = {
        'petFile': petFile,
        'dewormingHistory_list': dewormingHistory_list,
        'dewormingForm': dewormingForm,
    }

    return render(request, 'files/deworming_history_list.html', context)


def delete_deworming_history(request):
    dewormingHistory_id = request.POST.get('dewormingHistory_id', None)
    DewormingHistory.objects.filter(id=dewormingHistory_id).delete()
    return JsonResponse({})


def show_internment_history(request, pk):
    petFile = get_object_or_404(PetFile, pk=pk)
    petForm = PetForm(instance=petFile)
    context = {
        'petFile': petFile,
    }
    return render(request, 'files/show_internment_history.html', context)
