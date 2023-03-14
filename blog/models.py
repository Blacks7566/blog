from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE) # one to many relationship becaus one user can have multipul post but a post can only have one author

    def __str__(self):

        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    

