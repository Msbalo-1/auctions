from django.contrib.auth.models import User
from django.db import models
import uuid




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=300, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    profile_img = models.ImageField(null=True, blank=True, upload_to='profile_img/', default='profile_img/user-default.png')
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return self.username








class Product(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=250)
    price = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    img = models.ImageField(null=True, blank=True, default='default.jpg')
    vote = models.BooleanField(default=False)
    target_date = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)



    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created', 'price', 'vote']





