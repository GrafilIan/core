# Generated by Django 4.2.6 on 2023-10-26 04:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announcement_list', models.CharField(max_length=1000, null=True)),
                ('image_announcement', models.ImageField(blank=True, null=True, upload_to='media/images/')),
                ('document_announcement', models.FileField(blank=True, null=True, upload_to='media/documents/')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
