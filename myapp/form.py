from django import forms
# from froala_editor.widgets import FroalaEditor
from .models import *

class ProductForm(forms.ModelForm):
    images = forms.ImageField(widget=forms.FileInput(attrs={'multiple': True}))

    class Meta:
        model = Product
    #     fields = ['name', 'description', 'images']