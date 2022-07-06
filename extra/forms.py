from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from extra.models import Publisher,Category

class PublisherForm(ModelForm):
    class Meta:
        model=Publisher
        fields='__all__'

class CategoryForm(ModelForm):
    class Meta:
        model=Category
        fields='__all__'