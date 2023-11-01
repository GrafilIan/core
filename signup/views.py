from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import InternForm


@login_required
def add_intern_records(request):
    if request.method == 'POST':
        form = InternForm(request.POST, request.FILES)
        if form.is_valid():
            intern_record = form.save(commit=False)
            intern_record.user = request.user
            intern_record.form_filled_out = True  # Set form_filled_out to True
            intern_record.save()  # Save the changes to the database
            return redirect('intern_announcement_list')  # Redirect to the dashboard after successful form submission
    else:
        form = InternForm()

    return render(request, 'authentication/intern_create.html', {'form': form})


