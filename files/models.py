from django.db import models
import datetime


class Owner(models.Model):
    owner_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number_1 = models.CharField(max_length=100)
    phone_number_2 = models.CharField(max_length=100)
    phone_number_3 = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']


class PetFile(models.Model):
    pet_name = models.CharField(max_length=255)
    pet_img = models.ImageField(
        blank=True, upload_to='images/', default='images/no-image-found.png')
    sex = models.CharField(max_length=64)
    race = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    date_of_birth = models.DateField(blank=True, null=True)
    castrated = models.BooleanField(default=False)
    castration_date = models.DateField(blank=True, null=True)
    aggressive = models.BooleanField(default=False)
    description = models.TextField(default='')
    obs = models.TextField(default='')
    allergies = models.TextField(default='')
    # owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    # clinic_history = models.ForeignKey(
    #     ClinicHistory, on_delete=models.CASCADE)
    # vaccination_history = models.ForeignKey(
    #     Vaccination_history, on_delete=models.CASCADE)
    # deworming_history = models.ForeignKey(
    #     Deworming_history, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']


class ClinicHistory(models.Model):
    clinic_signs = models.CharField(max_length=255)
    treatments = models.CharField(max_length=255)
    obs = models.TextField(default='')
    petFile = models.ForeignKey(PetFile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class VaccinationHistory(models.Model):
    vaccine_name = models.CharField(max_length=255)
    date = models.DateField(default=datetime.date.today)
    next_date = models.DateField(default=datetime.date.today)
    petFile = models.ForeignKey(PetFile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class DewormingHistory(models.Model):
    antiparasitic_name = models.CharField(max_length=255)
    date = models.DateField(default=datetime.date.today)
    next_date = models.DateField(default=datetime.date.today)
    petFile = models.ForeignKey(PetFile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
