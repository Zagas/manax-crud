# encoding: utf-8
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now

from libmanax import depot

@python_2_unicode_compatible
class {{cookiecutter.object_name}}(models.Model):
    """{{cookiecutter.object_name}}
    """
    id = models.CharField(primary_key=True, max_length=6, default=depot.newid(6), editable=False)
    created = models.DateTimeField('created', default=now())
    modified = models.DateTimeField('modified', default=now())
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = '{{cookiecutter.object_slug}}'
        verbose_name_plural = '{{cookiecutter.object_slug}}'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = now()
        self.modified = now()
        super({{cookiecutter.object_name}}, self).save(*args, **kwargs)
