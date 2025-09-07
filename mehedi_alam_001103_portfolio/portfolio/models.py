from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserModel(AbstractUser):

    def __str__(self):
        return self.username
    

class ProfileModel(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, null=True, related_name='profile')
    fullName = models.CharField(max_length=150, null=True)
    phone = models.CharField(max_length=15, null=True)
    profilePhoto = models.ImageField(upload_to='profile-photo/', null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.user.username if self.user else "No User"

    

class ResumeModel(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='resumes/', blank=True, null=True)
    

    profile_pic=models.ImageField(upload_to="Media/Pro_pic",null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    portfolio_url = models.URLField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title or 'Untitled'


    

class ContactModel(models.Model):
    name=models.CharField(max_length=40,null=True)
    phone=models.PositiveIntegerField(null=True)
    message = models.TextField(blank=True, null=True)


    
    
    
    