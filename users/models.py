from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ImageField(upload_to="profile_images/", default="default_user.png")
    
    def __str__(self):
        return str(f"Profile of {str(self.user.first_name)}")