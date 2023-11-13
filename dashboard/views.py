from django.db.models import Sum
from django.shortcuts import render, get_object_or_404

from documents.models import WeeklyBin, Internship
from .forms import AnnouncementForm
from .models import Announcement
from signup.models import Intern_Records
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required


def create_announcement(request):
    if request.method == 'POST':
        announcement_form = AnnouncementForm(request.POST, request.FILES, prefix='announcement')

        if 'all_submit' in request.POST:
            if announcement_form.is_valid():
                announcement = announcement_form.save()
                announcement.save()

            return redirect('announcement_list')


    else:
        announcement_form = AnnouncementForm(prefix='announcement')

    context = {
        'announcement_form': announcement_form,
    }

    return render(request, 'dashboard/create_announcement.html', context)


@login_required
def announcement_list(request):
    announcements = Announcement.objects.all().order_by('-pub_date')

    course_records = Intern_Records.objects.filter(folder__isnull=True)
    interns = Intern_Records.objects.filter(folder__isnull=True)

    BSIT_records = Intern_Records.objects.filter(course='BSIT', folder__isnull=True)
    BSIS_records = Intern_Records.objects.filter(course='BSIS', folder__isnull=True)
    BSCS_records = Intern_Records.objects.filter(course='BSCS', folder__isnull=True)
    BSA_records = Intern_Records.objects.filter(course='BSA', folder__isnull=True)
    BSAIS_records = Intern_Records.objects.filter(course='BSAIS', folder__isnull=True)
    BPA_records = Intern_Records.objects.filter(course='BPA', folder__isnull=True)
    BSE_records = Intern_Records.objects.filter(course='BSE', folder__isnull=True)

    BSIT_count = BSIT_records.count()
    BSIS_count = BSIS_records.count()
    BSCS_count = BSCS_records.count()
    BSA_count = BSA_records.count()
    BSAIS_count = BSAIS_records.count()
    BPA_count = BPA_records.count()
    BSE_count = BSE_records.count()
    course_count = course_records.count()

    for intern in interns:
        intern.max_hours = intern.get_ojt_hours()
        intern.remaining_hours = intern.get_remaining_ojt_hours()
        intern.remaining_percentage = 100 - ((intern.remaining_hours / intern.max_hours) * 100)

    context = {
        'announcements': announcements,
        'BSIT_count': BSIT_count,
        'BSIS_count': BSIS_count,
        'BSCS_count': BSCS_count,
        'BSA_count': BSA_count,
        'BSAIS_count': BSAIS_count,
        'BPA_count': BPA_count,
        'BSE_count' : BSE_count,
        'course_count': course_count,
        'interns': interns,
    }

    return render(request, 'dashboard/admin_dashboard.html', context)

@login_required
def intern_announcement_list(request):
    user = request.user
    intern = get_object_or_404(Intern_Records, user=user)

    try:
        internship = Internship.objects.get(user=user)
        intern_records = Intern_Records.objects.get(user=user)
        interns = Intern_Records.objects.all()
        weekly_bins = WeeklyBin.objects.filter(internship=internship)
        max_hours = intern_records.get_ojt_hours()
        remaining_hours = intern_records.get_remaining_ojt_hours()
        remaining_percentage = ((max_hours - remaining_hours) / max_hours) * 100
        total_hours_rendered = weekly_bins.aggregate(Sum('rendered_hours'))['rendered_hours__sum'] or 0

        context = {
            'internship': internship,
            'total_hours_rendered': total_hours_rendered,
            'max_hours': max_hours,
            'remaining_hours': remaining_hours,
            'remaining_percentage': remaining_percentage,
            'interns': interns,
            'intern': intern,
        }
    except Internship.DoesNotExist:
        context = {}

    announcements = Announcement.objects.all().order_by('-pub_date')
    context['announcements'] = announcements

    return render(request, 'dashboard/intern_dashboard.html', context)



def delete_item(request, item_type, item_id):
    if item_type == 'announcement':
        item = get_object_or_404(Announcement, pk=item_id)
        if request.method == 'POST':
            item.delete()
            return redirect('announcement_list')
        # Handle deletion and redirection for announcements


    else:
        # Handle invalid item type
        pass

    if request.method == 'POST':
        item.delete()
        return redirect('announcement_list')

    context = {
        'item': item,
        'item_type': item_type.capitalize(),  # Capitalize for display
    }

    return render(request, 'dashboard/delete_item.html', context)


def delete_all_announcement(request):
    if request.method == 'POST':
        Announcement.objects.all().delete()

    return redirect('announcement_list')


