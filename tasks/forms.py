from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields =  {'titulo','description', 'imprtante'}
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'escribe un titulo'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'escribe una descripcion'}),
            'imprtante': forms.CheckboxInput(attrs={'class': 'form-check-input text-center'}),
        }