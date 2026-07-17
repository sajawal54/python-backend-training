from django.shortcuts import render , redirect , get_object_or_404
from .models import Student
from .forms import StudentForm
from django.contrib import messages
from django.core.paginator import Paginator


def students_list(request):

      students = Student.objects.all().order_by("name")

      paginator = Paginator(students, 4)

      page_number = request.GET.get("page")

      page_obj = paginator.get_page(page_number)

   


      context = {
       "page_obj": page_obj
         }


      return render(request , "students/index.html" , context)



def add_students(request):
   
   if request.method == "POST":
      form = StudentForm(request.POST)

      if form.is_valid():
         messages.success(request , "Student Added Successfully")
         form.save()
         return redirect("/students/")
      
   else:
      form = StudentForm()

   return render(request , "students/add_students.html" , {"form" : form})

def edit_student(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            messages.success(request , "Student Updated Successfully")
            form.save()
            return redirect("/students/")

    else:
        form = StudentForm(instance=student)

    return render(
        request,
        "students/edit_student.html",
        {"form": form}
    )

def delete_student(request, id):

    student = get_object_or_404(Student, id=id)

    student.delete()
    messages.success(request , "Student Deleted Successfully")

    return redirect("/students/")