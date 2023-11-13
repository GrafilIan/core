from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.db.models import Sum
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from documents.forms import FolderForm
from documents.models import Internship, WeeklyBin, Requirements, DailyTimeRecord, NarrativeReport, Post_Requirements, \
    Folder, Record
from signup.forms import InternStatusEditForm
from signup.models import Intern_Records
from .forms import UserDeleteForm

# Create your views here.
@login_required
@user_passes_test(lambda user: user.is_superuser)
def intern_list(request):
    folders = Folder.objects.all()
    if request.method == 'POST':
        form = UserDeleteForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data.get('user_id')
            try:
                user_to_delete = User.objects.get(id=user_id)
                user_to_delete.delete()
            except User.DoesNotExist:
                pass
    else:
        form = UserDeleteForm()

    if request.method == 'POST':
        folder_form = FolderForm(request.POST)
        if folder_form.is_valid():
            folder_form.save()
            return redirect('intern_list')
    else:
        folder_form = FolderForm()

    interns = Intern_Records.objects.filter(folder__isnull=True)  # Filter interns not associated with any folder

    for intern in interns:
        intern.max_hours = intern.get_ojt_hours()
        intern.remaining_hours = intern.get_remaining_ojt_hours()
        intern.remaining_percentage = 100 - ((intern.remaining_hours / intern.max_hours) * 100)

    return render(request, 'internlist/intern_list.html', {'interns': interns, 'form': form, 'folders': folders, 'folder_form': folder_form})

@login_required
@user_passes_test(lambda user: user.is_superuser)
def archive_intern(request, intern_id, folder_id):
    intern = get_object_or_404(Intern_Records, id=intern_id)
    folder = get_object_or_404(Folder, id=folder_id)

    Record.objects.create(name=intern.user.get_full_name(), folder=folder)
    intern.folder = folder
    intern.save()

    return redirect('intern_list')

@login_required
@user_passes_test(lambda user: user.is_superuser)
def intern_detail(request, intern_id):
    intern = get_object_or_404(Intern_Records, pk=intern_id)
    weekly_bins = WeeklyBin.objects.filter(internship__user=intern.user)
    requirements = Requirements.objects.filter(user=intern.user)
    daily_time_records = DailyTimeRecord.objects.filter(user=intern.user)
    narrative_reports = NarrativeReport.objects.filter(user=intern.user)
    post_requirements = Post_Requirements.objects.filter(user=intern.user)

    # Calculate max_hours, remaining_hours, and remaining_percentage for the specific intern
    intern.max_hours = intern.get_ojt_hours()
    intern.remaining_hours = intern.get_remaining_ojt_hours()
    intern.remaining_percentage = 100 - ((intern.remaining_hours / intern.max_hours) * 100)

    interns = Intern_Records.objects.all()

    total_hours_rendered = weekly_bins.aggregate(Sum('rendered_hours'))['rendered_hours__sum'] or 0

    # Handle form submission for editing intern status
    if request.method == 'POST':
        form = InternStatusEditForm(request.POST, instance=intern)
        if form.is_valid():
            form.save()
            return redirect('intern_list')  # Redirect to the intern_list or intern_detail as needed
    else:
        form = InternStatusEditForm(instance=intern)

    return render(request, 'internlist/intern_detail.html', {
        'intern': intern,
        'weekly_bins': weekly_bins,
        'requirements': requirements,
        'daily_time_records': daily_time_records,
        'narrative_reports': narrative_reports,
        'post_requirements': post_requirements,
        'interns': interns,
        'total_hours_rendered': total_hours_rendered,
        'form': form,  # Include the form in the context for rendering in the template
    })


@login_required
@user_passes_test(lambda user: user.is_superuser)
def admin_intern_detail(request, intern_id):
    intern = get_object_or_404(Intern_Records, pk=intern_id)
    weekly_bins = WeeklyBin.objects.filter(internship__user=intern.user)
    requirements = Requirements.objects.filter(user=intern.user)
    daily_time_records = DailyTimeRecord.objects.filter(user=intern.user)
    narrative_reports = NarrativeReport.objects.filter(user=intern.user)
    post_requirements = Post_Requirements.objects.filter(user=intern.user)

    # Calculate any additional data as needed

    return render(request, 'documents/forms/view_narrative.html', {
        'intern': intern,
        'weekly_bins': weekly_bins,
        'requirements': requirements,
        'daily_time_records': daily_time_records,
        'narrative_reports': narrative_reports,
        'post_requirements': post_requirements,
    })

@login_required
@user_passes_test(lambda user: user.is_superuser)
def view_requirements(request, intern_id):
    intern = get_object_or_404(Intern_Records, pk=intern_id)
    weekly_bins = WeeklyBin.objects.filter(internship__user=intern.user)
    requirements = Requirements.objects.filter(user=intern.user)


    # Calculate any additional data as needed

    return render(request, 'documents/forms/view_requirements.html', {
        'intern': intern,
        'weekly_bins': weekly_bins,
        'requirements': requirements,

    })

@login_required
@user_passes_test(lambda user: user.is_superuser)
def view_dtr(request, intern_id):
    intern = get_object_or_404(Intern_Records, pk=intern_id)
    weekly_bins = WeeklyBin.objects.filter(internship__user=intern.user)
    dtr = DailyTimeRecord.objects.filter(user=intern.user)

    # Calculate any additional data as needed

    return render(request, 'documents/forms/view_dtr.html', {
        'intern': intern,
        'weekly_bins': weekly_bins,
        'dtr': dtr,

    })

@login_required
@user_passes_test(lambda user: user.is_superuser)
def view_post_requirements(request, intern_id):
    intern = get_object_or_404(Intern_Records, pk=intern_id)
    weekly_bins = WeeklyBin.objects.filter(internship__user=intern.user)
    post_requirements = Post_Requirements.objects.filter(user=intern.user)

    # Calculate any additional data as needed

    return render(request, 'documents/forms/view_post_requirements.html', {
        'intern': intern,
        'weekly_bins': weekly_bins,
        'post_requirements': post_requirements,
    })

@login_required
@user_passes_test(lambda user: user.is_superuser)
def view_weekly_report(request, intern_id):
    intern = get_object_or_404(Intern_Records, pk=intern_id)
    weekly_bins = WeeklyBin.objects.filter(internship__user=intern.user)


    # Calculate any additional data as needed

    return render(request, 'documents/forms/view_weekly_report.html', {
        'intern': intern,
        'weekly_bins': weekly_bins,

    })

@login_required
@user_passes_test(lambda user: user.is_superuser)
def archive_selected_interns(request):
    if request.method == 'GET':
        intern_ids = request.GET.get('intern_ids', '').split(',')
        folder_id = request.GET.get('folder_id', None)

        if folder_id is None:
            return HttpResponseBadRequest('Invalid request. Missing folder_id.')

        folder = get_object_or_404(Folder, id=folder_id)

        interns = Intern_Records.objects.filter(id__in=intern_ids, folder__isnull=True)

        for intern in interns:
            Record.objects.create(name=intern.user.get_full_name(), folder=folder)
            intern.folder = folder
            intern.save()

        return HttpResponseRedirect(reverse('intern_list'))

    return HttpResponseBadRequest('Invalid request.')