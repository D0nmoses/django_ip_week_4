from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    occupants_count = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_neighbourhood(self):
        self.save()

    @classmethod
    def delete_neighbourhood(cls,neighbourhood):
        cls.objects.filter(neighbourhood=neighbourhood).delete()

class Business(models.Model):
    neighbourhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    address =models.CharField(max_length=100)
    contact = models.IntegerField()

    def __str__(self):
        return self.name

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='avatars/')
    neighbourhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.username

class Post(models.Model):
    post = models.TextField()
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood= models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)