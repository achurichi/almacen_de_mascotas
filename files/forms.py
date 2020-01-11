from django import forms

from .models import PetFile, Owner, ClinicHistory, ClinicHistoryImg, VaccinationHistory, DewormingHistory

from tempus_dominus.widgets import DatePicker

import datetime

SEX_CHOICES = [('Macho', 'Macho'), ('Hembra', 'Hembra')]


class PetForm(forms.ModelForm):
    sex = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=([('Macho', 'Macho'), ('Hembra', 'Hembra'), ]),
    )
    race = forms.CharField(required=False)
    date_of_birth = castration_date = forms.DateField(
        required=False,
        widget=DatePicker(
            options={
                'format': 'DD/MM/YYYY',
                'locale': 'es',
            }),
    )
    castrated = forms.BooleanField(required=False)
    aggressive = forms.BooleanField(required=False)
    description = forms.CharField(required=False, widget=forms.Textarea)
    obs = forms.CharField(required=False, widget=forms.Textarea)
    allergies = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = PetFile
        fields = [
            'pet_name',
            'pet_img',
            'sex',
            'race',
            'date_of_birth',
            'castrated',
            'castration_date',
            'aggressive',
            'description',
            'obs',
            'allergies',
        ]


class OwnerForm(forms.ModelForm):
    address = forms.CharField(required=False)
    phone_number_1 = forms.CharField(required=False)
    phone_number_2 = forms.CharField(required=False)
    phone_number_3 = forms.CharField(required=False)

    class Meta:
        model = Owner

        fields = [
            'owner_name',
            'address',
            'phone_number_1',
            'phone_number_2',
            'phone_number_3',
        ]


class ClinicHistoryForm(forms.ModelForm):
    date = forms.DateField(
        initial=datetime.date.today,
        widget=DatePicker(
            options={
                'format': 'DD/MM/YYYY',
                'locale': 'es',
            }),
    )
    abstract = forms.CharField(required=False)
    history = forms.CharField(required=False, widget=forms.Textarea)
    clinic_signs = forms.CharField(required=False, widget=forms.Textarea)
    diagnosis = forms.CharField(required=False, widget=forms.Textarea)
    treatments = forms.CharField(required=False, widget=forms.Textarea)
    obs = forms.CharField(required=False, widget=forms.Textarea)
    complementary_studies = forms.CharField(
        required=False, widget=forms.Textarea)

    class Meta:
        model = ClinicHistory

        fields = [
            'date',
            'abstract',
            'history',
            'clinic_signs',
            'diagnosis',
            'treatments',
            'obs',
            'complementary_studies',
        ]


class ClinicHistoryImgForm(forms.ModelForm):
    class Meta:
        model = ClinicHistoryImg
        fields = ['image', ]


class VaccinationHistoryForm(forms.ModelForm):
    vaccine_name = forms.CharField(required=False)
    date = forms.DateField(
        initial=datetime.date.today,
        widget=DatePicker(
            options={
                'format': 'DD/MM/YYYY',
                'locale': 'es',
            }),
    )
    next_date = forms.DateField(
        required=False,
        widget=DatePicker(
            options={
                'format': 'DD/MM/YYYY',
                'locale': 'es',
            }),
    )

    class Meta:
        model = VaccinationHistory

        fields = [
            'vaccine_name',
            'date',
            'next_date',
        ]


class DewormingHistoryForm(forms.ModelForm):
    antiparasitic_name = forms.CharField(required=False)
    date = forms.DateField(
        initial=datetime.date.today,
        widget=DatePicker(
            options={
                'format': 'DD/MM/YYYY',
                'locale': 'es',
            }),
    )
    next_date = forms.DateField(
        required=False,
        widget=DatePicker(
            options={
                'format': 'DD/MM/YYYY',
                'locale': 'es',
            }),
    )

    class Meta:
        model = DewormingHistory

        fields = [
            'antiparasitic_name',
            'date',
            'next_date',
        ]
