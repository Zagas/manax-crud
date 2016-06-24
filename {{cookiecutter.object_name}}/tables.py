{% if cookiecutter.list_as_table == "y" %}
import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor

from .models import {{ cookiecutter.object_name }}

class {{ cookiecutter.object_name }}Table(tables.Table):
    """{{ cookiecutter.object_name }} Table
    """
    name = tables.LinkColumn('{{ cookiecutter.app_slug }}:{{ cookiecutter.object_slug }}detail',
                               args=[A('id')])
      
    class Meta:
        model = {{ cookiecutter.object_name }}
        fields = ('id', 'name') # fields to diplay
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}
{% endif %}
