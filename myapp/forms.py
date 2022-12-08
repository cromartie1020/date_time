from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime

class Date_time_form(forms.Form):
     name=forms.CharField()
     email=forms.EmailField(label='E-mail')
     date=forms.DateField(widget=AdminDateWidget())
     time=forms.DateField(widget=AdminTimeWidget())
     date_time=forms.DateField(widget=AdminSplitDateTime())


 
