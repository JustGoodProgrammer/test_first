from django import forms


'''class AdvertisementForm(forms.Form):
    title = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    auction = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=True)
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))'''

'''from django.db import models
from django.forms import CheckboxInput, ModelForm, Textarea, FileInput

class Models(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length = None, widget = Textarea(attrs={'class': 'form-control'}))
    price = models.DecimalField(max_digits = 7, decimal_places = 2)
    auction = models.BooleanField(widget = CheckboxInput(attrs={'class': 'form-check-input'}), required = True)
    image = models.ImageField(widget = FileInput(attrs={'class': 'form-control'}))

    def __str__(self): 
        return self.title

class AdvertisementForm(ModelForm):
    class Meta:
        model = Models
        fields = ['__all__']'''

from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Advertisement

def validation_question(value):
    if value[0] == '?':
        raise ValidationError(
            ('%(value)s starts with ?, that not allowed'),
            params={'value': value},
        )
 
class AdvertisementForm(ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'auction', 'image']
        widgets = {
            'title': forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validation_question]),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'auction': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }
