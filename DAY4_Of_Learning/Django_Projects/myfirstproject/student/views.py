from django.shortcuts import render ,redirect
from .models import Student
from django.core.paginator import Paginator
from .forms import StudentForm
from django.contrib import messages 



def student(request):
       students = Student.objects.all()
       paginator = Paginator(students , 2)

       page_number = request.GET.get("page")

       page_obj = paginator.get_page(page_number)
       context = {
              "page_obj" : page_obj
       }

       return render(request , "student/index.html" , context)


def add_student(request):
    
#     if request.method == "POST":
#           name = request.POST.get("name")
#           age = request.POST.get("age")
#           email = request.POST.get("email")

#           Student.objects.create(
#                 name = name,
#                 age = age,
#                 email = email
#           )
        
#           return redirect("/student/")

      if request.method == "POST":
             form = StudentForm(request.POST)

             if form.is_valid():
              
              form.save()

              messages.success(request , "Student Added Successfully")

              return redirect("/student/")
      else:
           form = StudentForm()

      return render(request, "student/add_student.html" , {"form" : form})

# Create your views here.
