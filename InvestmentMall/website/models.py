import email
from django.db import models

# Create your models here.
class clientLeads(models.Model):
    product_choice = (
        ("1","PR1"),
        ("2","PR2"),
        ("3","PR3"),
        ("4","PR4"),
        ("5","PR5"),
    )
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=10)
    product = models.CharField(max_length=1, choices=product_choice)
    location = models.CharField(max_length=70)
