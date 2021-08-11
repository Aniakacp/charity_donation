from django import forms
from django.contrib.admin.widgets import AdminTimeWidget
from django.contrib.auth.models import User

from used.models import Category, Institution


class CategoryForm(forms.Form):
    name =forms.ModelMultipleChoiceField(queryset=Category.objects.all(), required=False, label=False,
                                         widget=forms.CheckboxSelectMultiple())


class AdressForm(forms.Form):
    street= forms.CharField(max_length=100,label='Street')
    city= forms.CharField(max_length=100)
    post_code= forms.CharField(max_length=50)
    phone= forms.IntegerField()


class CollectForm(forms.Form):
    date= forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time= forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    notes= forms.CharField(widget=forms.Textarea)

class InstitutionForm(forms.Form):
    radio = forms.ModelChoiceField(widget=forms.RadioSelect, queryset= Institution.objects.all())

class BagsForm(forms.Form):
    bags= forms.IntegerField(label=False)

