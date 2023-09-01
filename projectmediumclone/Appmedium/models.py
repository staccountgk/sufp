from django.db import models
from django.contrib.auth.models import User

class PostCreate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="PostImage")
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostCreate, on_delete=models.CASCADE,null=True)
    text = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
class Profil(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    about = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="ProfilImage", default="person.png")

    def __str__(self):
        return self.user.username