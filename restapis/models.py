from django.db import models

# Create your models here.

class Pizzas(models.Model):
    pizza_type=models.CharField(max_length=20)
    pizza_size=models.CharField(max_length=20)
    pizza_topping=models.CharField(max_length=20)


