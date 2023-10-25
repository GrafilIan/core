from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import InternForm
from .models import Intern_Records


@login_required
def add_intern_records(request):
    if request.method == 'POST':
        form = InternForm(request.POST, request.FILES)
        if form.is_valid():
            intern_record = form.save(commit=False)
            intern_record.user = request.user
            intern_record.form_filled_out = True
            intern_record.save()
            return redirect('dashboard.html')  # Redirect to the dashboard after successful form submission

    else:
        form = InternForm()

    return render(request, 'authentication/intern_create.html', {'form': form})

