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


    context = {
        'announcements': announcements,
    }

    return render(request, 'dashboard/admin_dashboard.html', context)

@login_required
def intern_announcement_list(request):
    user = request.user

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
        }
    except Internship.DoesNotExist:
        context = {}

    announcements = Announcement.objects.all().order_by('-pub_date')
    context['announcements'] = announcements

    return render(request, 'dashboard/intern_dashboard.html', context)



def delete_item(request, item_type, item_id):
    if item_type == 'announcement':
        item = get_object_or_404(Announcement, pk=item_id)
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


