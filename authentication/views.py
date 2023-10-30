# import this to require login
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# import this for sending email to user
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from authentication.forms import UserRegistrationForm
from dashboard.models import Announcement
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from signup.models import Intern_Records



@login_required(login_url='login')
def homepage(request):
    if request.user.is_superuser:
        if request.method == 'POST' and 'delete_announcement' in request.POST:
            announcement_id = request.POST.get('announcement_id')
            announcement = get_object_or_404(Announcement, pk=announcement_id)
            announcement.delete()
            return redirect('announcement_list')

        announcements = Announcement.objects.all().order_by('-pub_date')
        context = {
            'announcements': announcements,
        }

        return render(request, 'dashboard/admin_dashboard.html', context)

    # Check if the user has already filled out the form
    try:
        intern_record = Intern_Records.objects.get(user=request.user)
        if intern_record.form_filled_out:
            return render(request, 'studentbase.html')  # Redirect to the dashboard if the form is filled out
    except Intern_Records.DoesNotExist:
        pass  # Intern record doesn't exist, indicating the form has not been filled out

    # If the user is not a superuser and hasn't filled out the form, redirect to the form page
    return redirect('add_intern_records')



def register(request):
    form = UserRegistrationForm()


    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            # email user with activation link
            current_site = get_current_site(request)
            mail_subject = "Activate your account."

            # the message will render what is written in authentication/email_activation/activate_email_message.html
            message = render_to_string('authentication/email_activation/activate_email_message.html', {
                    'user': form.cleaned_data['username'],
                    #'intern': intern_form.cleaned_data['student_id'],
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':  default_token_generator.make_token(user),
                })
            to_email = form.cleaned_data['email']
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            messages.success(request, 'Account created successfully. Please check your email to activate your account.')
            return redirect('login')
        else:
            messages.error(request, 'Account creation failed. Please try again.')


    return render(request, 'authentication/register.html',{
        'form': form,
    })

# to activate user from email
def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'authentication/email_activation/activation_successful.html')
    else:
        return render(request, 'authentication/email_activation/activation_unsuccessful.html')


