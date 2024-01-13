from django.db import models

# Create your models here.

class Word(models.Model):
    text=models.CharField(max_length=100)
    
    def __str__(self):
        return self.text
    
    
class UserDataCompany(models.Model):
    text=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    cameracompany=models.CharField(max_length=20)
    latitude=models.CharField(max_length=20)
    longitude=models.CharField(max_length=20)
    phone=models.CharField(max_length=12)
    range=models.IntegerField(default=0,null=True)
    location=models.CharField(max_length=50)
    pincode=models.IntegerField(default=0,null=True)
    mobile=models.CharField(max_length=12)
    
    def __str__(self):
        return self.text
    
    
    
class UploadedImage(models.Model):
    image=models.ImageField(upload_to="image/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    
