# Generated by Django 4.2.4 on 2023-11-26 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_mediform_guardian_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mediform',
            name='premedics',
        ),
    ]
