from django.shortcuts import render
from signup.models import Intern_Records

# Create your views here.
def intern_list(request):
    interns = Intern_Records.objects.all()
    return render(request, 'internlist/intern_list.html', {'interns': interns})