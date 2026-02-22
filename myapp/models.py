from django.db import models
from django.contrib.auth.models import User
#Create your model here
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(null=True, blank=True)
    contact = models.CharField(max_length=20, null=True, blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='profiles/', null=True, blank=True)

    def __str__(self):
        return self.user.username
