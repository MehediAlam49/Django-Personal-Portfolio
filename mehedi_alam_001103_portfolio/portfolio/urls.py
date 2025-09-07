from django.urls import path
from portfolio.views import *


urlpatterns = [
    path('', loginPage, name='loginPage'),
    path('registerPage/', registerPage, name='registerPage'),
    path('logoutPage/', logoutPage, name='logoutPage'),
    path('changePassword/', changePassword, name='changePassword'),

    path('profile/', profile, name='profile'),
    path('updateProfile/', updateProfile, name='updateProfile'),
    
    path('home/', home, name='home'),
    path('addResumeField/', addResume,name="addResumeField"),
    path('viewResumeList/', viewResumeList,name="viewResumeList"),
    path('resume_delete/<str:id>', resume_delete,name="resume_delete"),
    path('resume_detail/<str:id>', resume_detail,name="resume_detail"),
    path('resume_edit/<str:id>', resume_edit,name="resume_edit"),
    path('contact', contact_view,name="contact"),
]