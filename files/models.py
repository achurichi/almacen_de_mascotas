from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

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
    pet_img = ProcessedImageField(upload_to='images/',
                                  processors=[ResizeToFill(600, 400)],
                                  format='JPEG',
                                  blank=True,
                                  default='images/no-image-found.jpg')
    # pet_img = models.ImageField(
    #     blank=True, upload_to='images/', default='images/no-image-found.png')
    sex = models.CharField(max_length=64)
    race = models.CharField(max_length=255, blank=True)
    age = models.IntegerField(default=0, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    castrated = models.BooleanField(default=False)
    castration_date = models.DateField(blank=True, null=True)
    aggressive = models.BooleanField(default=False)
    description = models.TextField(default='', blank=True)
    obs = models.TextField(default='', blank=True)
    allergies = models.TextField(default='', blank=True)
    # clinic_history = models.ForeignKey(
    #     ClinicHistory, on_delete=models.CASCADE)
    # vaccination_history = models.ForeignKey(
    #     Vaccination_history, on_delete=models.CASCADE)
    # deworming_history = models.ForeignKey(
    #     Deworming_history, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pet_name

    class Meta:
        ordering = ['created_at']


@receiver(post_delete, sender=PetFile)
def submission_delete(sender, instance, **kwargs):
    if instance.pet_img != "images/no-image-found.jpg":
        instance.pet_img.delete(False)


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
