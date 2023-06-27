from django.shortcuts import render
from .models import Student
from .forms import StudentForm
from .forms import ReadForm
from django.forms.models import model_to_dict

# Home Page:
def home(request):
    context = {}
    if request.method == "POST":
        id = request.POST.get("id")
        Student.objects.filter(id = id).delete()
        context['deleted'] = True
    return render(request, "home.html", context = context)


# Create a new entity:
def create(request):

    context = {}
    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():

            # Recieve data from form and Make model and save it:
            new_student = Student.objects.create(
                first_name = request.POST.get("first_name"),
                last_name = request.POST.get("last_name"),
                sex = request.POST.get("sex"),
                grade = request.POST.get("grade"),
                birth_date = request.POST.get("birth_date"),
                register_date = request.POST.get("register_date"),
                graduation_date = request.POST.get("graduation_date"),
                address = request.POST.get("address"),
                phone = request.POST.get("phone")
            )
            new_student.save()
            id = new_student.id
            

            context['created'] = True
            context['id'] = id
            context['form'] = form
            return render(request, "create.html",  context = context)
        
        # If the form is not valid:
        else:
            context['created'] = False
            context['form'] = form
            return render(request, "create.html", context = context)

    # When you come with GET:
    else:
        form = StudentForm()
        context['created'] = False
        context['form'] = form


    return render(request, "create.html", context = context)



# Retrive student's data:
def read(request):
    context = {}
    if request.method == "POST":
        form = ReadForm(request.POST)
        if form.is_valid():
            phone = request.POST.get('phone')
            student = Student.objects.get(phone = phone)
            meta_dict = model_to_dict(student, fields=[field.name for field in student._meta.fields])
            fields = list(meta_dict.keys())
            values = list(meta_dict.values())
            context['values'] = values
            context['fields'] = fields
            context['student'] = student
            context['form'] = form
            return render(request, "read.html", context = context)
        
        else:
            context['form'] = form
            return render(request, "read.html", context = context)
    
    else:
        form = ReadForm()
        context['form'] = form


    return render(request, "read.html", context = context)


def update(request):
    context = {}
    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():
            id = request.POST.get('id')
            student = Student.objects.filter(id = id).update(
                first_name = request.POST.get("first_name"),
                last_name = request.POST.get("last_name"),
                sex = request.POST.get("sex"),
                grade = request.POST.get("grade"),
                birth_date = request.POST.get("birth_date"),
                register_date = request.POST.get("register_date"),
                graduation_date = request.POST.get("graduation_date"),
                address = request.POST.get("address"),
                phone = request.POST.get("phone")
            )

            context['updated'] = True
            context['student'] = student
            return render(request, "update.html", context = context)
        
        else:
            context['form'] = form
            return render(request, "update.html", context = context)
    
    else:
        id = request.GET.get('id')
        student = Student.objects.get(id = id)
        initial = {
            'first_name':student.first_name,
            'last_name':student.last_name,
            'sex':student.sex,
            'grade':student.grade,
            'phone':student.phone
        }
        form = StudentForm(initial=initial)
        context['form'] = form
        context['student'] = student

    return render(request, "update.html", context = context)
    
