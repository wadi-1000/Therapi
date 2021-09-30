from .models import Articles,Appointments
from django.forms import ModelForm
from django import forms



class UploadNewArticle(forms.ModelForm):
    class Meta:
        model=Articles
        fields=['title','pic','content','author','categories']

class MakeAppointment(forms.ModelForm):
    class Meta:
        model=Appointments
        fields=['client','psychologists','date','condition']