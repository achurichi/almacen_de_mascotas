# Generated by Django 3.0.1 on 2020-01-13 15:02

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True, default='')),
                ('sale_price', models.FloatField(blank=True)),
                ('purchase_price', models.FloatField(blank=True)),
                ('last_purchase', models.DateField(blank=True, null=True)),
                ('quantity', models.CharField(blank=True, max_length=255)),
                ('obs', models.TextField(blank=True, default='')),
                ('image', imagekit.models.fields.ProcessedImageField(default='images/no-image-found.jpg', upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
