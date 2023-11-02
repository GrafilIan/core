from django.db.models import Sum, Max
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from signup.models import Intern_Records
from .forms import InternshipForm, WeeklyBinForm, AddBinForm
from .models import Internship, WeeklyBin
from django.http import Http404
# Create your views here.
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
            weekly_bin.week_number = week_number

            weekly_bin.save()
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
        'form': form
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


