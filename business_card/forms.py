from django import forms
from .models import BusinessCard

class BusinessCardForm(forms.ModelForm):
    class Meta:
        model = BusinessCard
        fields = [
            'name', 'designation', 'description', 'company_name', 'contact_number',
            'whatsapp_number', 'email', 'instagram', 'facebook', 'linkdin', 'twitter', 
            'reddit', 'youtube', 'pinterest', 'company_logo', 'profile_image', 
            'primary_color', 'seconday_color'
        ]
        widgets = {
            'primary_color': forms.TextInput(attrs={'type': 'color', 'class': 'form-control form-control-color'}),
            'seconday_color': forms.TextInput(attrs={'type': 'color', 'class': 'form-control form-control-color'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to non-color fields
        text_fields = [
            'name', 'designation', 'description', 'company_name', 'contact_number',
            'whatsapp_number', 'email', 'instagram', 'facebook', 'linkdin', 
            'twitter', 'reddit', 'youtube', 'pinterest'
        ]
        for field in text_fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        
        # Add file input classes to image fields
        for field in ['company_logo', 'profile_image']:
            self.fields[field].widget.attrs.update({'class': 'form-control-file'})

