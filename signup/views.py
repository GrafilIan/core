from django.shortcuts import render, redirect
from .models import Intern
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import InternForm

@login_required
def intern_record(request):
    if request.method == 'POST':
        form = InternForm(request.POST, request.FILES)
        if form.is_valid():
            intern = form.save(commit=False)  # Create the Intern instance but don't save it to the database yet
            intern.user = request.user  # Associate the Intern with the currently logged-in user
            intern.save()  # Now save the Intern instance with the associated User

            # Optionally, you can do additional processing or redirect the user to another page.
            return redirect('success_page')  # Replace 'success_page' with the URL name of your success page
    else:
        form = InternForm()


    return render(request, 'authentication/intern_create.html', {'form':form})