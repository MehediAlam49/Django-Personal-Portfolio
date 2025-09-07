from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['fullName','phone','profilePhoto']

        widgets = {
            'fullName': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full Name'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number'
            }),
            'profilePhoto': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }



class ResumeForm(forms.ModelForm):
    class Meta:
        model = ResumeModel
        fields = [
            'title', 'description', 'file','profile_pic', 
            'name', 'email', 'phone_number', 
            'address', 'linkedin_url', 'github_url', 
            'portfolio_url', 'education', 'experience', 'skills'
        ]
        widgets = {
        'title': forms.TextInput(attrs={'placeholder': 'Resume Title', 'class': 'form-control'}),
        'description': forms.Textarea(attrs={'placeholder': 'Brief Description', 'class': 'form-control', 'rows': 3}),
        
        'profile_pic': forms.ClearableFileInput(attrs={'multiple': False, 'class': 'form-control-file'}),
        
        'file': forms.ClearableFileInput(attrs={'multiple': False, 'class': 'form-control-file'}),
        'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-control'}),
        'phone_number': forms.TextInput(attrs={'placeholder': 'Your Phone Number', 'class': 'form-control'}),
        'address': forms.Textarea(attrs={'placeholder': 'Your Address', 'class': 'form-control', 'rows': 3}),
        'linkedin_url': forms.URLInput(attrs={'placeholder': 'LinkedIn URL', 'class': 'form-control'}),
        'github_url': forms.URLInput(attrs={'placeholder': 'GitHub URL', 'class': 'form-control'}),
        'portfolio_url': forms.URLInput(attrs={'placeholder': 'Portfolio URL', 'class': 'form-control'}),
        'education': forms.Textarea(attrs={'placeholder': 'Your Education', 'class': 'form-control', 'rows': 3}),
        'experience': forms.Textarea(attrs={'placeholder': 'Your Experience', 'class': 'form-control', 'rows': 3}),
        'skills': forms.Textarea(attrs={'placeholder': 'Your Skills', 'class': 'form-control', 'rows': 3}),
    }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].required = False  

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = "__all__"

        widgets = {
        'name': forms.TextInput(attrs={'placeholder': 'Enter your name', 'class': 'form-control'}),
        'phone': forms.TextInput(attrs={'placeholder': 'Enter your phone', 'class': 'form-control'}),
        'message': forms.Textarea(attrs={'placeholder': 'Write a message', 'class': 'form-control', 'rows': 3}),
        }
    
