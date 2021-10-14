from django import forms
from django.db.models.base import Model
from django.forms import ModelForm, fields
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # fields = ('title', 'complete')
        # fields = '__all__'
        exclude = ('user', )
