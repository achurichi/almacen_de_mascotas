# Generated by Django 3.0.1 on 2020-01-05 19:57

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0011_auto_20200104_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petfile',
            name='pet_img',
            field=imagekit.models.fields.ProcessedImageField(default='images/no-image-found.jpg', upload_to='images/'),
        ),
    ]