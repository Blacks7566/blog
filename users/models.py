from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ImageField(upload_to='profile_pic',default='profile_pic/default.jpg')

    def __str__(self):
        return self.user.username + ' profile'
    
    def save(self):
        super().save()
        
        img = Image.open(self.profile.path)
        
        if img.height > 300 or img.width > 300:
            new_size = (300,300)
            img.thumbnail(new_size)
            img.save(self.profile.path)