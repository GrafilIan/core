# Generated by Django 4.2.6 on 2023-11-02 15:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_weeklybin_rendered_hours'),
    ]

    operations = [
        migrations.AddField(
            model_name='weeklybin',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
