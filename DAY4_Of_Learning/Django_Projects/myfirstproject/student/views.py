from django.shortcuts import render


def student(request):
  return render(request , "student/index.html")

# Create your views here.
