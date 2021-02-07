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
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

class ProductImg(models.Model):
    image = ProcessedImageField(verbose_name='Foto',
                                upload_to='images/',
                                processors=[ResizeToFit(
                                    1280, 720, mat_color=(32, 40, 41))],
                                format='JPEG')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        try:
            this = ProductImg.objects.get(id=self.id)
            this.image.delete(save=False)
        except:
            pass
        super(ProductImg, self).save(*args, **kwargs)


@receiver(post_delete, sender=ProductImg)
def submission_delete_ProductImg(sender, instance, **kwargs):
    instance.image.delete(False)
