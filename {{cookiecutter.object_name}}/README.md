# manax-crud howto

{% if cookiecutter.list_as_table == "y" %}
edit config/settings/common.py

THIRD_PARTY_APPS = (
[..]
    'django_tables2', # tables layouts
[..]
)

edit requirements/apps.txt

[..]
# {{ cookiecutter.app_slug }}
django-tables2==1.2.2
[..]
{% endif %}






