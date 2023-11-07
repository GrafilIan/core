from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import InternForm, InternStatusEditForm
from .models import Intern_Records


@login_required
def add_intern_records(request):
    # Check if the user has already submitted a form
    existing_record = Intern_Records.objects.filter(user=request.user).first()

    if request.method == 'POST':
        if existing_record:
            # If the user has already submitted a form, load the existing data for editing
            form = InternForm(request.POST, request.FILES, instance=existing_record)
        else:
            # If the user hasn't submitted a form, create a new form
            form = InternForm(request.POST, request.FILES)

        if form.is_valid():
            intern_record = form.save(commit=False)
            intern_record.user = request.user
            intern_record.form_filled_out = True
            intern_record.save()
            return redirect('view_internship_info')

    else:
        # If the user has an existing record, load the data into the form for editing
        if existing_record:
            form = InternForm(instance=existing_record)
        else:
            form = InternForm()

    return render(request, 'authentication/intern_create.html', {'form': form})


@user_passes_test(lambda user: user.is_superuser)
def edit_intern_status(request, intern_id):
    intern = Intern_Records.objects.get(id=intern_id)

    if request.method == 'POST':
        form = InternStatusEditForm(request.POST, instance=intern)
        if form.is_valid():
            form.save()
            return redirect('intern_list')
    else:
        form = InternStatusEditForm(instance=intern)

    return render(request, 'internlist/edit_intern_status.html', {'form': form, 'intern': intern})
