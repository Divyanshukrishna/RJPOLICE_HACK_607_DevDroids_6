from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Word)

@admin.register(UserDataCompany)
class UserDataCompanyAdmin(admin.ModelAdmin):
    list_display=['text' , 'cameracompany', 'email', 'range', 'pincode']

admin.site.register(UploadedImage)