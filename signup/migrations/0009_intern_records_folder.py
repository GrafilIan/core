# Generated by Django 4.2.6 on 2023-11-09 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0005_archivefolder'),
        ('signup', '0008_intern_records_academic_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='intern_records',
            name='folder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='documents.archivefolder'),
        ),
    ]
