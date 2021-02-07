# Generated by Django 3.1.6 on 2021-02-07 20:58

import datetime
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('abstract', models.CharField(max_length=255)),
                ('history', models.TextField(blank=True, default='')),
                ('clinic_signs', models.TextField(blank=True, default='')),
                ('diagnosis', models.TextField(blank=True, default='')),
                ('treatments', models.TextField(blank=True, default='')),
                ('obs', models.TextField(blank=True, default='')),
                ('complementary_studies', models.TextField(blank=True, default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='InternmentDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('clinic_signs', models.TextField(blank=True, default='')),
                ('obs', models.TextField(blank=True, default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone_number_1', models.CharField(max_length=100)),
                ('phone_number_2', models.CharField(max_length=100)),
                ('phone_number_3', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='PetFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.CharField(max_length=255)),
                ('pet_img', imagekit.models.fields.ProcessedImageField(default='images/no-image-found.jpg', upload_to='images/')),
                ('sex', models.CharField(max_length=64)),
                ('species', models.CharField(blank=True, default='', max_length=64)),
                ('race', models.CharField(blank=True, max_length=255)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('castrated', models.BooleanField(default=False)),
                ('castration_date', models.DateField(blank=True, null=True)),
                ('aggressive', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, default='')),
                ('obs', models.TextField(blank=True, default='')),
                ('allergies', models.TextField(blank=True, default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='files.owner')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='VaccinationHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_name', models.CharField(max_length=255)),
                ('date', models.DateField(default=datetime.date.today)),
                ('next_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('petFile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='files.petfile')),
            ],
        ),
        migrations.CreateModel(
            name='InternmentTreatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drug', models.CharField(max_length=255)),
                ('drug_hour', models.TimeField(blank=True, null=True)),
                ('be_notified', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('internmentDay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='files.internmentday')),
            ],
        ),
        migrations.CreateModel(
            name='InternmentHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_date', models.DateField(default=datetime.date.today)),
                ('exit_date', models.DateField(blank=True, null=True)),
                ('is_interned', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('petFile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='files.petfile')),
            ],
        ),
        migrations.CreateModel(
            name='InternmentDayImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='images/', verbose_name='Foto')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('internmentDay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='files.internmentday')),
            ],
        ),
        migrations.AddField(
            model_name='internmentday',
            name='internmentHistory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='files.internmenthistory'),
        ),
        migrations.CreateModel(
            name='DewormingHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('antiparasitic_name', models.CharField(max_length=255)),
                ('date', models.DateField(default=datetime.date.today)),
                ('next_date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('petFile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='files.petfile')),
            ],
        ),
        migrations.CreateModel(
            name='ClinicHistoryImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='images/', verbose_name='Foto')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('clinicHistory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='files.clinichistory')),
            ],
        ),
        migrations.AddField(
            model_name='clinichistory',
            name='petFile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='files.petfile'),
        ),
    ]
