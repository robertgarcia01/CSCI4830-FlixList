from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'watches']
        # Apply CSS styles
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter name of Movie',
            }),
            'watches': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter view count',
                }),
        }
