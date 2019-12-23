from django import forms

from .models import PetFile, Owner

import datetime


class PetForm(forms.ModelForm):
    now = datetime.datetime.now()

    sex = forms.CharField(required=False)
    race = forms.CharField(required=False)
    # age = forms.IntegerField(required=False, initial=0)
    date_of_birth = castration_date = forms.DateField(
        required=False,
        # initial=None,

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


# class PetForm(forms.ModelForm):
#     name = forms.CharField(label='name', max_length=100)
#     sex = forms.CharField(label='name', max_length=64)

#     name = forms.CharField(label='name', max_length=255)
#     sex = forms.CharField(label='sex', max_length=64)
#     race = forms.CharField(label='race', max_length=255)
#     age = forms.IntegerField(label='age')
#     date_of_birth = forms.DateTimeField(label='date_of_birth')
#     castrated = forms.BooleanField(label='castrated')
#     castration_date = forms.DateTimeField(label='castration_date')
#     description = forms.CharField(label='description')
#     obs = forms.CharField(label='obs')
