from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Sum, Max
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test

from internlist.forms import UserDeleteForm
from signup.models import Intern_Records
from .forms import InternshipForm, WeeklyBinForm, AddBinForm, RequirementsForm, DTRForm, NarrativeForm, \
    PostRequirementsForm
from .models import Internship, WeeklyBin, Requirements, DailyTimeRecord, NarrativeReport, Post_Requirements
from django.http import Http404
from .models import Folder, Record
from .forms import FolderForm, RecordForm

@login_required
def intern_schedule(request):

    return render(request, 'documents/schedule.html')

def enter_internship_info(request):
    if request.method == 'POST':
        internship_form = InternshipForm(request.POST)
        if internship_form.is_valid():
            internship = internship_form.save(commit=False)
            internship.user = request.user
            internship.save()
            return redirect('view_internship_info')
    else:
        internship_form = InternshipForm()

    return render(request, 'documents/enter_internship_info.html', {'internship_form': internship_form})

# For dispalying Weekly Submission Bins
def view_internship_info(request):
    user = request.user
    try:
        internship = Internship.objects.get(user=user)
    except Internship.DoesNotExist:
        return redirect('enter_internship_info')

    intern_records = Intern_Records.objects.get(user=user)
    interns = Intern_Records.objects.all()

    # Check if the user has created the first 4 weekly bins, and if not, create them
    for week_number in range(1, 5):
        weekly_bin, created = WeeklyBin.objects.get_or_create(internship=internship, week_number=week_number)
        if created:
            # If the bin was just created, save it to ensure it has the necessary fields set
            weekly_bin.save()

    weekly_bins = WeeklyBin.objects.filter(internship=internship)

    max_hours = intern_records.get_ojt_hours()  # Get the required hours based on the course

    # Calculate remaining hours and percentage as before
    remaining_hours = intern_records.get_remaining_ojt_hours()
    remaining_percentage = ((max_hours - remaining_hours) / max_hours) * 100
    total_hours_rendered = weekly_bins.aggregate(Sum('rendered_hours'))['rendered_hours__sum'] or 0

    if request.method == 'POST':
        form = AddBinForm(request.POST, request.FILES)
        if form.is_valid():
            weekly_bin = form.save(commit=False)
            weekly_bin.internship = internship

            # Retrieve the week number from the form data
            week_number = form.cleaned_data.get('week_number')

            # Set the week_number for the new bin
            existing_bin = WeeklyBin.objects.filter(internship=internship, week_number=week_number).first()
            if existing_bin:
                # Bin already exists, you can show an error message here
                messages.error(request, f"A weekly bin for week {week_number} already exists.")
            else:
                weekly_bin.week_number = week_number
                weekly_bin.save()
                # You can add a success message here if needed
                messages.success(request, "Weekly bin added successfully.")
                # Redirect to avoid resubmission
            return redirect('view_internship_info')
            # You can add a success message here if needed
        else:
            # Handle form errors, you can add error messages if needed
            pass
    else:
        form = AddBinForm()

    return render(request, 'documents/view_internship_info.html', {
        'internship': internship,
        'weekly_bins': weekly_bins,
        'max_hours': max_hours,
        'remaining_hours': remaining_hours,
        'remaining_percentage': remaining_percentage,
        'total_hours_rendered': total_hours_rendered,
        'form': form,
        'interns': interns
    })


#For Creating Weekly Report
def add_to_weekly_bin(request, week_number):
    user = request.user
    try:
        internship = Internship.objects.get(user=user)
        weekly_bin = WeeklyBin.objects.get(internship=internship, week_number=week_number)
    except (Internship.DoesNotExist, WeeklyBin.DoesNotExist):
        return redirect('view_internship_info')

    if request.method == 'POST':
        form = WeeklyBinForm(request.POST, request.FILES, instance=weekly_bin)
        if form.is_valid():
            form.save()

            # Calculate the total rendered hours for all weeks
            total_rendered_hours = WeeklyBin.objects.filter(internship=internship).aggregate(Sum('rendered_hours'))['rendered_hours__sum']

            # Update the remaining hours based on the total required hours and rendered hours
            intern_records = Intern_Records.objects.get(user=user)
            max_hours = intern_records.get_ojt_hours()
            intern_records.weekly_hours = total_rendered_hours
            intern_records.save()

            # Calculate remaining hours and percentage
            remaining_hours = intern_records.get_remaining_ojt_hours()
            remaining_percentage = ((max_hours - remaining_hours) / max_hours) * 100

            return redirect('view_internship_info')
    else:
        form = WeeklyBinForm(instance=weekly_bin)

    return render(request, 'documents/add_to_weekly_bin.html', {'form': form,
                                                                'week_number': week_number})

def add_weekly_bin(request):
    user = request.user
    try:
        internship = Internship.objects.get(user=user)
    except Internship.DoesNotExist:
        return redirect('enter_internship_info')

    if request.method == 'POST':
        form = AddBinForm(request.POST, request.FILES)
        if form.is_valid():
            weekly_bin = form.save(commit=False)
            weekly_bin.internship = internship

            # Retrieve the week number from the form data
            week_number = form.cleaned_data.get('week_number')

            # Set the week_number for the new bin
            weekly_bin.week_number = week_number

            weekly_bin.save()
            return redirect('view_internship_info')  # Redirect to view_internship_info to display the updated list
    else:
        form = AddBinForm()

    return render(request, 'documents/view_internship_info.html', {'form': form})

@login_required
def upload_requirements(request):

    if request.method == 'POST':
        form = RequirementsForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('upload_requirements')
    else:
        form = RequirementsForm()

    if request.method == 'POST' and 'delete_requirement' in request.POST:
        requirement_id = request.POST.get('delete_requirement')
        requirement_to_delete = get_object_or_404(Requirements, id=requirement_id, user=request.user)
        requirement_to_delete.delete()
        return redirect('upload_requirements')

    requirements = Requirements.objects.filter(user=request.user)

    return render(request, 'documents/forms/upload_requirements.html', {'form': form, 'requirements': requirements})

def upload_dtr(request):

    if request.method == 'POST':
        form = DTRForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('upload_dtr')
    else:
        form = DTRForm()

    dtr = DailyTimeRecord.objects.filter(user=request.user)

    return render(request, 'documents/forms/upload_dtr.html', {'form': form, 'dtr': dtr})


def upload_narrative(request):

    if request.method == 'POST':
        form = NarrativeForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('upload_narrative')
    else:
        form = NarrativeForm()

    narrative = NarrativeReport.objects.filter(user=request.user)

    return render(request, 'documents/forms/upload_narrative.html', {'form': form, 'narrative': narrative})



@login_required
def upload_post_requirements(request):
    if request.method == 'POST':
        form = PostRequirementsForm(request.POST, request.FILES)

        # Upload post requirement
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('upload_post_requirements')

        # Delete post requirement
        elif 'delete_post_requirement' in request.POST:
            post_id = request.POST.get('delete_post_requirement')
            post_to_delete = get_object_or_404(Post_Requirements, id=post_id, user=request.user)
            post_to_delete.delete()
            return redirect('upload_post_requirements')
    else:
        form = PostRequirementsForm()

    post_requirements = Post_Requirements.objects.filter(user=request.user)

    return render(request, 'documents/forms/upload_post_requirements.html', {'form': form, 'post_requirements': post_requirements})

def folder_list(request):
    folders = Folder.objects.all()
    return render(request, 'documents/archive/folder_list.html', {'folders': folders})

def create_folder(request):
    if request.method == 'POST':
        form = FolderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('folder_list')
    else:
        form = FolderForm()
    return render(request, 'documents/archive/create_folder.html', {'form': form})

def folder_detail(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id)
    records = Record.objects.filter(folder=folder)
    interns = Intern_Records.objects.filter(folder=folder)

    if request.method == 'POST':
        # Handle form submission
        form = UserDeleteForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data.get('user_id')
            # Perform the delete action here
            try:
                user_to_delete = User.objects.get(id=user_id)
                user_to_delete.delete()
            except User.DoesNotExist:
                # If the user doesn't exist, you can log or display a message
                pass
    else:
        form = UserDeleteForm()

    return render(request, 'documents/archive/folder_detail.html', {'folder': folder, 'records': records, 'interns': interns, 'form': form})


