from django import forms
from .models import airbnb
class FormPost(forms.ModelForm):
    
   class Meta:
      model=airbnb
      #fields='__all__'
      exclude=['house_photos',]
      verbose_name= 'room'
      verbose_name_plural = 'rooms'