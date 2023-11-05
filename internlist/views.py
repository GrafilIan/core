from django.contrib.auth.decorators import user_passes_test
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404
from documents.models import Internship, WeeklyBin, Requirements, DailyTimeRecord, NarrativeReport, Post_Requirements
from signup.models import Intern_Records

# Create your views here.
def intern_list(request):
    interns = Intern_Records.objects.all()

    for intern in interns:
        intern.max_hours = intern.get_ojt_hours()
        intern.remaining_hours = intern.get_remaining_ojt_hours()
        intern.remaining_percentage = 100 - ((intern.remaining_hours / intern.max_hours) * 100)

    return render(request, 'internlist/intern_list.html', {'interns': interns})

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

    return render(request, 'internlist/intern_detail.html', {
        'intern': intern,
        'weekly_bins': weekly_bins,
        'requirements': requirements,
        'daily_time_records': daily_time_records,
        'narrative_reports': narrative_reports,
        'post_requirements': post_requirements,
        'interns': interns,
        'total_hours_rendered': total_hours_rendered,
    })


def is_admin(user):
    return user.is_authenticated and user.is_superuser

@user_passes_test(is_admin)
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

@user_passes_test(is_admin)
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

@user_passes_test(is_admin)
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

@user_passes_test(is_admin)
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

@user_passes_test(is_admin)
def view_weekly_report(request, intern_id):
    intern = get_object_or_404(Intern_Records, pk=intern_id)
    weekly_bins = WeeklyBin.objects.filter(internship__user=intern.user)


    # Calculate any additional data as needed

    return render(request, 'documents/forms/view_weekly_report.html', {
        'intern': intern,
        'weekly_bins': weekly_bins,

    })
