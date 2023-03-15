
from django.db import models
import uuid
from users.models import Profile

class Product(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=250)
    price = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    img = models.ImageField(null=True, blank=True, default='default.jpg')
    vote = models.BooleanField(default=False)
    target_date = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)



    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created', 'price', 'vote']


class Order(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.customer}-{self.name}'


