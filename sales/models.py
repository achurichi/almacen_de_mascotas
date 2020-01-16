from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from imagekit.processors import ResizeToFit


class Product(models.Model):
    product_id = models.CharField(max_length=255, blank=True)
    product_type = models.CharField(max_length=255, blank=True)
    brand = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    sale_price = models.FloatField(blank=True, null=True)
    purchase_price = models.FloatField(blank=True, null=True)
    last_purchase = models.DateField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    obs = models.TextField(default='', blank=True)
    image = ProcessedImageField(upload_to='images/',
                                processors=[ResizeToFill(800, 500)],
                                format='JPEG',
                                default='images/no-image-found.jpg')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
