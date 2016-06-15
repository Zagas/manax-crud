from django import forms

from .models import {{cookiecutter.object_name}}

class {{cookiecutter.object_name}}Form(forms.ModelForm):
    class Meta:
        model = {{cookiecutter.object_name}}
        fields = ['name', ]

