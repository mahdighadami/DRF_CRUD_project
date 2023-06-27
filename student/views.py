from django.shortcuts import render
from .models import Student
from .forms import StudentForm

# Home Page:
def home(request):
    return render(request, "home.html")


# Create a new entity:
def create(request):

    context = {}
    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():

            # Recieve data from form:
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            sex = request.POST.get("sex")
            grade = request.POST.get("grade")
            birth_date = request.POST.get("birth_date")
            register_date = request.POST.get("register_date")
            graduation_date = request.POST.get("graduation_date")
            address = request.POST.get("address")
            phone = request.POST.get("phone")
            date = request.POST.get("date")

            # Make model and save it:
            new_student = Student.objects.create(
                first_name = first_name,
                last_name = last_name,
                sex = sex,
                grade = grade,
                birth_date = birth_date,
                register_date = register_date,
                graduation_date = graduation_date,
                address = address,
                phone = phone
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
    