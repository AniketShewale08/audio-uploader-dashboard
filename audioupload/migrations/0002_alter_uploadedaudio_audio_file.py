# Generated by Django 4.0.7 on 2023-08-26 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audioupload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedaudio',
            name='audio_file',
            field=models.FileField(upload_to=''),
        ),
    ]
