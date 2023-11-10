from django.db import models
from django.contrib.auth.models import User

# Seller Models.
 
class Vendor(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    address=  models.CharField(null = True)

    def __str__(self):
        return self.user.username

#Category models

class DressCategory(models.Model):
    title = models.CharField(max_length=255)
    detail = models.TextField(null = True)

    def __str__(self):
        return self.title

#Dress models 



class Dress(models.Model):
    title = models.CharField(max_length=255)
    detail = models.TextField(null = True)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title