# Generated by Django 5.1.6 on 2025-02-23 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='file',
            field=models.FileField(upload_to='media_files/'),
        ),
    ]
