from django.db import models
import uuid
from users.models import Profile
from PIL import Image

class Product(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=250)
    price = models.PositiveIntegerField(null=True)
    description = models.TextField(null=True, blank=True)
    img = models.ImageField(null=True, blank=True, default='default.jpg')
    vote = models.BooleanField(default=False)
    target_date = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created', 'price', ]


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        image = Image.open(self.img.path)
        image = image.resize((450, 300))
        image.save(self.img.path)










class Order(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    price = models.PositiveIntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f'{self.customer}-{self.product}'



