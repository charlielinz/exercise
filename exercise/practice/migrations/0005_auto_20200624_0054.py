# Generated by Django 3.0.7 on 2020-06-23 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0004_job'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='job',
            new_name='position',
        ),
    ]
