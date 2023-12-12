from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Seller)
admin.site.register(models.Customer)

admin.site.register(models.ProductCategory)

admin.site.register(models.Order)
admin.site.register(models.OrderItems)


admin.site.register(models.Product)
admin.site.register(models.Robe)
admin.site.register(models.Shoe)
admin.site.register(models.Accessory)

admin.site.register(models.CustomerAddress)

admin.site.register(models.ProductRating)
admin.site.register(models.CustomerRating)