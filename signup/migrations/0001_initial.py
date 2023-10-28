# Generated by Django 4.2.6 on 2023-10-24 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intern',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('student_id', models.CharField(max_length=200, null=True, verbose_name='Student ID')),
                ('middle_name', models.CharField(max_length=200, null=True, verbose_name='Middle Name')),
                ('suffix', models.CharField(max_length=200, null=True, verbose_name='suffix')),
                ('present_address', models.CharField(max_length=200, null=True, verbose_name='Present Address')),
                ('semester', models.CharField(choices=[('1st Semester', '1st Semester'), ('2nd Semester', '2nd Semester')], max_length=20, null=True)),
                ('course', models.CharField(choices=[('BSIT', 'BSIT'), ('BSIS', 'BSIS'), ('BSCS', 'BSCS'), ('BSA', 'BSA'), ('BSAIS', 'BSAIS'), ('BPA', 'BPA')], max_length=10, null=True, verbose_name='Course')),
                ('year_level', models.CharField(max_length=200, null=True, verbose_name='Year Level')),
                ('block', models.CharField(max_length=200, null=True, verbose_name='Block')),
                ('company_name', models.CharField(max_length=200, null=True, verbose_name='Company')),
                ('address', models.CharField(max_length=200, null=True, verbose_name='Address')),
                ('contact_person', models.CharField(max_length=200, null=True, verbose_name='Contact Person')),
                ('contact_number', models.CharField(max_length=200, null=True, verbose_name='Contact Number')),
                ('profile_image', models.ImageField(default='images/default_profile_image.png', upload_to='profile_images/')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('Not Placed', 'Not Placed'), ('On OJT', 'On OJT'), ('Late OJT', 'Late OJT'), ('On Leave', 'On Leave'), ('Suspended', 'Suspended'), ('Resigned', 'Resigned'), ('Extended', 'Extended'), ('Terminated', 'Terminated'), ('Completed', 'Completed')], max_length=20, null=True)),
            ],
        ),
    ]