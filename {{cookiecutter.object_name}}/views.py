from django.shortcuts import get_object_or_404, redirect, render

from .models import {{cookiecutter.object_name}}
from .forms import {{cookiecutter.object_name}}Form
{% if cookiecutter.list_as_table == "y" %}
from .tables import {{cookiecutter.object_name}}Table
{% endif %}

# {{cookiecutter.object_name}}

def {{cookiecutter.object_name}}Home(request):
    """
    """
    context = {}
    return render(request, '{{cookiecutter.app_slug}}/{{cookiecutter.object_slug}}/home.html', context)  

def {{cookiecutter.object_name}}List(request):
    """List {{cookiecutter.object_slug}}
    """
    {{cookiecutter.object_slug}}_list = {{cookiecutter.object_name}}.objects.all()

    {% if cookiecutter.list_as_table == "y" %}
    table = {{cookiecutter.object_name}}Table({{cookiecutter.object_slug}}_list)
    RequestConfig(request).configure(table)
    {% endif %}

    context = { {% if cookiecutter.list_as_table == "y" %}'table': table, {% endif %}'{{cookiecutter.object_slug}}_list': {{cookiecutter.object_slug}}_list}
    return render(request, '{{cookiecutter.app_slug}}/{{cookiecutter.object_slug}}/list.html', context)  

def {{cookiecutter.object_name}}Create(request):
    """Create a new {{cookiecutter.object_slug}}
    """
    if request.method == 'POST':
        form = {{cookiecutter.object_name}}Form(data=request.POST)
        if form.is_valid():
            {{cookiecutter.object_slug}} = form.save()
            return redirect('{{cookiecutter.app_slug}}:{{cookiecutter.object_slug}}home')
    else:
        form = {{cookiecutter.object_name}}Form()
    context = {'form': form, 'create': True}
    return render(request, '{{cookiecutter.app_slug}}/{{cookiecutter.object_slug}}/form.html', context)  

def {{cookiecutter.object_name}}Detail(request, id):
    """Detail on {{cookiecutter.object_slug}}
    """
    {{cookiecutter.object_slug}} = get_object_or_404({{cookiecutter.object_name}}, id=id)
    context = {'{{cookiecutter.object_slug}}': {{cookiecutter.object_slug}}}
    return render(request, '{{cookiecutter.app_slug}}/{{cookiecutter.object_slug}}/detail.html', context)  

def {{cookiecutter.object_name}}Update(request, id):
    """Update a {{cookiecutter.object_slug}}
    """
    {{cookiecutter.object_slug}} = get_object_or_404({{cookiecutter.object_name}}, id=id)
    if request.method == 'POST':
        form = {{cookiecutter.object_name}}Form(instance={{cookiecutter.object_slug}}, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('{{cookiecutter.app_slug}}:{{cookiecutter.object_slug}}home')
    else:
        form = {{cookiecutter.object_name}}Form(instance={{cookiecutter.object_slug}})
    context = {'form': form, 'create': False}
    return render(request, '{{cookiecutter.app_slug}}/{{cookiecutter.object_slug}}/form.html', context)  

def {{cookiecutter.object_name}}Delete(request, id):
    """Delete a {{cookiecutter.object_slug}}
    """
    context = {}
    return render(request, '{{cookiecutter.app_slug}}/{{cookiecutter.object_slug}}/delete.html', context)
