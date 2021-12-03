from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse


class EmployeeView(ListView):
    queryset = Employee.objects.all()
    context_object_name = 'employees'
    template_name = 'employee/list.html'


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')

    if 'term' in request.GET:
        qs = Employee.objects.filter(first_name__icontains=request.GET.get('term'))
        names = []
        for employee in qs:
            names.append(employee.first_name)
        return JsonResponse(names, safe=False)

    form = EmployeeForm()
    context = {'form': form}

    return render(request, 'employee/create.html', context)


class EditEmployee(UpdateView):
    model = Employee
    template_name = 'employee/update.html'
    fields = '__all__'
    success_url = reverse_lazy('list')


class RemoveEmployee(DeleteView):
    model = Employee
    template_name = 'employee/delete.html'
    success_url = reverse_lazy('list')

# class AddEmployee(CreateView):
#     model = Employee
#     template_name = 'employee/create.html'
#     fields = '__all__'
#     success_url = reverse_lazy('list')


# def autocomplete(request):
#     if 'term' in request.GET:
#         qs = Employee.objects.filter(first_name__istartswith=request.GET.get('term'))
#         names = []
#         for employee in qs:
#             names.append(employee.first_name)
#
#     return render(request, 'employee/create.html')
