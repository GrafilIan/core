# Generated by Django 4.2.6 on 2023-10-25 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0005_alter_intern_records_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='intern_records',
            name='form_filled_out',
            field=models.BooleanField(default=False),
        ),
    ]
