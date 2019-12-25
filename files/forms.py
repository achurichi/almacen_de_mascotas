from django import forms

from .models import PetFile, Owner

import datetime

SEX_CHOICES = [('Macho', 'Macho'), ('Hembra', 'Hembra')]


class PetForm(forms.ModelForm):
    now = datetime.datetime.now()

    sex = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=([('Macho', 'Macho'), ('Hembra', 'Hembra'), ]),
    )
    race = forms.CharField(required=False)
    date_of_birth = castration_date = forms.DateField(
        required=False,
        widget=forms.SelectDateWidget(
            empty_label=("Año", "mes", "día"),
            years=range(now.year, now.year - 40, -1),
        )
    )
    castrated = forms.BooleanField(required=False)
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
            'age',
            'date_of_birth',
            'castrated',
            'castration_date',
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
