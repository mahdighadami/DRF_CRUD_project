from django.shortcuts import render
from .models import Student
from .forms import StudentForm

# Create your views here.
def home(request):
    return render(request, "home.html")

def create(request):
    context = {}
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            context['created'] = True
            context['form'] = form
            return render(request, "create.html", context = context)
        else:
            context['created'] = False
            context['form'] = form
            return render(request, "create.html", context = context)

    else:
        form = StudentForm()
        context['created'] = False
        context['form'] = form
    return render(request, "create.html", context = context)

def read(request):
    pass