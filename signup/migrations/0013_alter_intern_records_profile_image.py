# Generated by Django 4.2.6 on 2023-11-13 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0012_alter_intern_records_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intern_records',
            name='profile_image',
            field=models.ImageField(upload_to='profile_images/'),
        ),
    ]
