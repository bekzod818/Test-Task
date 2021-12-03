from django.urls import path
from .views import EmployeeView, EditEmployee, RemoveEmployee, add_employee

urlpatterns = [
    path("", EmployeeView.as_view(), name="list"),
    path("add/", add_employee, name="create"),
    path("edit/<int:pk>/", EditEmployee.as_view(), name="update"),
    path("delete/<int:pk>/", RemoveEmployee.as_view(), name="delete")
]
