from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email_address', 'phone_number', 'message')
        widgets = {
            'name': forms.TextInput(
                attrs={'class':'form-control', 'id':'name', 'type':'text', 'placeholder':'Enter your name...', 'data-sb-validations':'required'}),
            'email_address': forms.EmailInput(
                attrs={'class':'form-control', 'id':'email', 'type':'email', 'placeholder':'Enter your email...', 'data-sb-validations':'required,email'}),
            'phone_number': forms.NumberInput(
                attrs={'class':'form-control', 'id':'phone', 'type':'tel', 'placeholder':'Enter your phone number...', 'data-sb-validations':'required'}),
            'message': forms.Textarea(
                attrs={'class':'form-control', 'id':'message', 'placeholder':'Enter your message here...', 'style':'height: 12rem', 'data-sb-validations':'required'}),
        }
