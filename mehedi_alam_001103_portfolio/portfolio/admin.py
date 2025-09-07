from django.contrib import admin
from portfolio.models import *

# Register your models here.
admin.site.register(CustomUserModel)
admin.site.register(ProfileModel)
admin.site.register(ResumeModel)
admin.site.register(ContactModel)