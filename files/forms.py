from django import forms

from .models import PetFile, Owner, ClinicHistory, ClinicHistoryImg, VaccinationHistory, DewormingHistory, InternmentHistory, InternmentDay, InternmentTreatment, InternmentDayImg

from tempus_dominus.widgets import DatePicker

import datetime

SEX_CHOICES = [('Macho', 'Macho'), ('Hembra', 'Hembra')]


class PetForm(forms.ModelForm):
    species = forms.CharField(required=False)
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
            },
            attrs={
                'autocomplete': 'off'
            },
        ),
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
            'species',
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
            },
            attrs={
                'autocomplete': 'off'
            },
        ),
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
            },
            attrs={
                'autocomplete': 'off'
            },
        ),
    )
    next_date = forms.DateField(
        required=False,
        widget=DatePicker(
            options={
                'format': 'DD/MM/YYYY',
                'locale': 'es',
            },
            attrs={
                'autocomplete': 'off'
            },
        ),
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
            },
            attrs={
                'autocomplete': 'off'
            },
        ),
    )
    next_date = forms.DateField(
        required=False,
        widget=DatePicker(
            options={
                'format': 'DD/MM/YYYY',
                'locale': 'es',
            },
            attrs={
                'autocomplete': 'off'
            },
        ),
    )

    class Meta:
        model = DewormingHistory

        fields = [
            'antiparasitic_name',
            'date',
            'next_date',
        ]


class InternmentHistoryForm(forms.ModelForm):
    entry_date = forms.DateField(
        initial=datetime.date.today,
        widget=DatePicker(
            options={
                'format': 'DD/MM/YYYY',
                'locale': 'es',
            },
            attrs={
                'autocomplete': 'off'
            },
        ),
    )
    exit_date = forms.DateField(
        required=False,
        widget=DatePicker(
            options={
                'format': 'DD/MM/YYYY',
                'locale': 'es',
            },
            attrs={
                'autocomplete': 'off'
            },
        ),
    )
    is_interned = forms.BooleanField(initial=True, required=False)

    class Meta:
        model = InternmentHistory

        fields = [
            'entry_date',
            'exit_date',
            'is_interned',
        ]


class InternmentDayForm(forms.ModelForm):
    date = forms.DateField(
        initial=datetime.date.today,
        widget=DatePicker(
            options={
                'format': 'DD/MM/YYYY',
                'locale': 'es',
            },
            attrs={
                'autocomplete': 'off'
            },
        ),
    )
    clinic_signs = forms.CharField(required=False, widget=forms.Textarea)
    obs = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = InternmentDay

        fields = [
            'date',
            'clinic_signs',
            'obs',
        ]


class InternmentTreatmentForm(forms.ModelForm):
    drug_hour = forms.DateField(
        initial=datetime.date.today,
        widget=DatePicker(
            options={
                'format': 'DD/MM/YYYY',
                'locale': 'es',
            },
            attrs={
                'autocomplete': 'off'
            },
        ),
    )
    be_notified = forms.BooleanField(required=False)

    class Meta:
        model = InternmentTreatment

        fields = [
            'drug',
            'drug_hour',
            'be_notified',
        ]


class InternmentDayImgForm(forms.ModelForm):
    class Meta:
        model = InternmentDayImg
        fields = ['image', ]
