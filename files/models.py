from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from imagekit.processors import ResizeToFit

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
                                  processors=[ResizeToFill(800, 500)],
                                  format='JPEG',
                                  default='images/no-image-found.jpg')
    sex = models.CharField(max_length=64)
    species = models.CharField(max_length=64, default='', blank=True)
    race = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    castrated = models.BooleanField(default=False)
    castration_date = models.DateField(blank=True, null=True)
    aggressive = models.BooleanField(default=False)
    description = models.TextField(default='', blank=True)
    obs = models.TextField(default='', blank=True)
    allergies = models.TextField(default='', blank=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        try:
            this = PetFile.objects.get(id=self.id)
            if this.pet_img != self.pet_img and this.pet_img != "images/no-image-found.jpg":
                this.pet_img.delete(save=False)
        except:
            pass
        super(PetFile, self).save(*args, **kwargs)

    def __str__(self):
        return self.pet_name

    class Meta:
        ordering = ['created_at']


@receiver(post_delete, sender=PetFile)
def submission_delete(sender, instance, **kwargs):
    if instance.pet_img != "images/no-image-found.jpg":
        instance.pet_img.delete(False)


class ClinicHistory(models.Model):
    date = models.DateField(default=datetime.date.today)
    abstract = models.CharField(max_length=255)
    history = models.TextField(default='', blank=True)
    clinic_signs = models.TextField(default='', blank=True)
    diagnosis = models.TextField(default='', blank=True)
    treatments = models.TextField(default='', blank=True)
    obs = models.TextField(default='', blank=True)
    complementary_studies = models.TextField(default='', blank=True)
    petFile = models.ForeignKey(PetFile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class ClinicHistoryImg(models.Model):
    image = ProcessedImageField(verbose_name='Foto',
                                upload_to='images/',
                                processors=[ResizeToFit(
                                    1280, 720, mat_color=(32, 40, 41))],
                                format='JPEG')
    clinicHistory = models.ForeignKey(ClinicHistory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        try:
            this = ClinicHistoryImg.objects.get(id=self.id)
            this.image.delete(save=False)
        except:
            pass
        super(ClinicHistoryImg, self).save(*args, **kwargs)


@receiver(post_delete, sender=ClinicHistoryImg)
def submission_delete_ClinicHistoryImg(sender, instance, **kwargs):
    instance.image.delete(False)


class VaccinationHistory(models.Model):
    vaccine_name = models.CharField(max_length=255)
    date = models.DateField(default=datetime.date.today)
    next_date = models.DateField(blank=True, null=True)
    petFile = models.ForeignKey(PetFile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class DewormingHistory(models.Model):
    antiparasitic_name = models.CharField(max_length=255)
    date = models.DateField(default=datetime.date.today)
    next_date = models.DateField(blank=True, null=True)
    petFile = models.ForeignKey(PetFile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class InternmentHistory(models.Model):
    entry_date = models.DateField(default=datetime.date.today)
    exit_date = models.DateField(blank=True, null=True)
    is_interned = models.BooleanField(default=True)
    petFile = models.ForeignKey(PetFile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class InternmentDay(models.Model):
    date = models.DateField(default=datetime.date.today)
    clinic_signs = models.TextField(default='', blank=True)
    obs = models.TextField(default='', blank=True)
    internmentHistory = models.ForeignKey(
        InternmentHistory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class InternmentTreatment(models.Model):
    drug = models.CharField(max_length=255)
    drug_hour = models.TimeField(blank=True, null=True)
    be_notified = models.BooleanField(default=True)
    internmentDay = models.ForeignKey(InternmentDay, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class InternmentDayImg(models.Model):
    image = ProcessedImageField(verbose_name='Foto',
                                upload_to='images/',
                                processors=[ResizeToFit(
                                    1280, 720, mat_color=(32, 40, 41))],
                                format='JPEG')
    internmentDay = models.ForeignKey(InternmentDay, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        try:
            this = InternmentDayImg.objects.get(id=self.id)
            this.image.delete(save=False)
        except:
            pass
        super(InternmentDayImg, self).save(*args, **kwargs)


@receiver(post_delete, sender=InternmentDayImg)
def submission_delete_InternmentDayImg(sender, instance, **kwargs):
    instance.image.delete(False)
