from django.shortcuts import render, get_object_or_404
from documents.models import Internship, WeeklyBin, Requirements, DailyTimeRecord, NarrativeReport, Post_Requirements
from signup.models import Intern_Records

# Create your views here.
def intern_list(request):
    interns = Intern_Records.objects.all()
    return render(request, 'internlist/intern_list.html', {'interns': interns})

def intern_detail(request, intern_id):
    intern = get_object_or_404(Intern_Records, pk=intern_id)
    weekly_bins = WeeklyBin.objects.filter(internship__user=intern.user)
    requirements = Requirements.objects.filter(user=intern.user)
    daily_time_records = DailyTimeRecord.objects.filter(user=intern.user)
    narrative_reports = NarrativeReport.objects.filter(user=intern.user)
    post_requirements = Post_Requirements.objects.filter(user=intern.user)
    return render(request, 'internlist/intern_detail.html', {
        'intern': intern,
        'weekly_bins': weekly_bins,
        'requirements': requirements,
        'daily_time_records': daily_time_records,
        'narrative_reports': narrative_reports,
        'post_requirements': post_requirements,
    })
