# Generated by Django 4.2.6 on 2023-11-03 02:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('documents', '0003_weeklybin_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requirements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requirement', models.CharField(choices=[('Acceptance Form for OJT', 'Acceptance Form for OJT'), ('Internship Agreement', 'Internship Agreement'), ('Student Information Sheet', 'Student Information Sheet'), ('Parent Consent', 'Parent Consent'), ('Barangay Clearance', 'Barangay Clearance'), ('Police Clearance', 'Police Clearance'), ('Parent ID', 'Parent ID'), ('Medical Certificate', 'Medical Certificate'), ('Cedula', 'Cedula')], max_length=300)),
                ('document_image', models.ImageField(upload_to='documents/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post_Requirements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_requirement', models.CharField(choices=[('Monitoring Evaluation Sheet', 'Monitoring Evaluation Sheet'), ('Merit of Rating', 'Merit of Rating'), ('Student Feedback Form', 'Student Feedback Form'), ('Supervisor Feedback Form', 'Supervisor Feedback Form')], max_length=300)),
                ('document_image', models.ImageField(upload_to='documents/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NarrativeReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Narrative_Number', models.PositiveIntegerField(null=True)),
                ('Narrative_Text', models.TextField()),
                ('document_submission', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DailyTimeRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DTR_Number', models.PositiveIntegerField(null=True)),
                ('DTR_submission', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]