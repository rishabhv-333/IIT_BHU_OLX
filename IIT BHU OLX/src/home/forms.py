from product import models
from django import forms

class newad(forms.ModelForm):
    class Meta:
        model=models.Product
        fields="__all__"
        # fields = ('name', 'condition','category','brand','description','price','image')
