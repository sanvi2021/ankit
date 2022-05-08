from dataclasses import fields
from django import forms
from .models import clientLeads

class ClientForm(forms.ModelForm):
    class Meta:
        model = clientLeads
        fields = '__all__'

        widgets ={
            'name': forms.TextInput(attrs={'class':'form-control','placholder':'Enter Your Name'}),
            'email': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your valid Email Id'}),
            'phone': forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your valid Mobile Number'}),
            'product': forms.Select(attrs={'class':'form-control'}),
            'location': forms.Textarea(attrs={'class':'form-control','placeholder':'Enter Your Address'})
        }

    