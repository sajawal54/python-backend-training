from django.urls import path

from . import views

urlpatterns = [
  path("" , views.students_list),
  path("add-students/" , views.add_students),
  path("edit-student/<int:id>/", views.edit_student , name = "edit_student"),
  path("delete-student/<int:id>/", views.delete_student , name = "delete_student"),
]