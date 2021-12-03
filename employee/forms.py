from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['section'].empty_label = 'Choose section'
        self.fields['lang'].empty_label = 'Choose language'

    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input', 'id': 'first_name', 'name': 'first_name'})
        }
