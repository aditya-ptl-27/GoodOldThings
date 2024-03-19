from django import forms
# from froala_editor.widgets import FroalaEditor
# from django.forms.widgets import MultiWidget, FileInput
from .widgets import MultiFileInput
from .models import *

class ProductForm(forms.ModelForm):
    # images = forms.ImageField(widget=forms.FileInput(attrs={'multiple': True}))
    # images = forms.ImageField(widget=MultiFileInput)

    class Meta:
        model = Product
        fields = ['user', 'p_category', 'p_name', 'p_description', 'p_price']
        CATEGORY_CHOICES = [
        ('Phone', 'Phone'),
        ('Laptop', 'Laptop'),
        ('Camera', 'Camera'),
        ('Travel_Bag', 'Travel Bag'),
    ]

        p_category = forms.ChoiceField(choices=CATEGORY_CHOICES)
        p_description = forms.Textarea(attrs={'rows': 5, 'cols': 40})

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']