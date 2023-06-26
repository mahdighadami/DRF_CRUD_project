from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Student
from .forms import StudentForm

# Create your views here.

def create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/thanks/")
    else:
        form = StudentForm()
    return render(request, "home.html", {"form" : form})