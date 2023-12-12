from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from datetime import timedelta

# Modèle pour les vendeurs
class Seller(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.user.username

# Modèle pour les catégories de robes
class ProductCategory(models.Model):
    title = models.CharField(max_length=255)
    detail = models.TextField(null=True)

    def __str__(self):
        return self.title

# Modèle de base pour les produits
class Product(models.Model):
    STATUS_CHOICES = [
        ('Unavailable', 'Non disponible'),
        ('Rented', 'Déjà loué'),
        ('Available', 'Disponible')
    ]
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='Available')

    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True)
    seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    detail = models.TextField(null=True)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=255, null=True)
    stock = models.IntegerField(default=1)



    def __str__(self):
        return self.title
    
    def is_recent(self):
        if self.created_at:
            return timezone.now() - self.created_at <= timedelta(days=30)
        return False
    
# Modèle pour les robes
class Robe(Product):
    WIDTH_CHOICES = [('XS', 'Extra Small'), ('S', 'Small'), ('M','Medium'), ('L','Large') ,('XL','ExtraLarge'), ('XXL','DoubleExtraLarge') ]  # Ajoutez d'autres tailles ici
    width = models.PositiveSmallIntegerField(null=True)
    height = models.PositiveSmallIntegerField(  null=True )
    size = models.CharField(max_length=3, choices=WIDTH_CHOICES)

# Modèle pour les chaussures
class Shoe(Product):
    size = models.IntegerField()

# Modèle pour les accessoires
class Accessory(Product):
    pass
    # Champs spécifiques aux accessoires si nécessaire

# Modèle pour les clients
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=True)
    mobile = models.PositiveBigIntegerField()

    def __str__(self):
        return self.user.username

# Modèle pour les commandes
class Order(models.Model):
    STATUS = [('Payment Declined', 'Payment Declined'),('Payment Pending', 'Payment Pending'),('Refund', 'Refund'),('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')]
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=255, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f'Order {self.id} - {self.status}'

# Modèle pour les articles commandés
class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, related_name='items', null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)  # Lien polymorphique
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.product.title} - Quantity: {self.quantity}'
#Customer adressess

class CustomerAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer_address')
    address = models.TextField()
    default_address = models.BooleanField(default=False)

    def __str__(self):
        return self.address

#Product rating

class ProductRating(models.Model):
    customer=models.ForeignKey(Customer, on_delete= models.CASCADE, related_name="rating_customer")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_ratings')
    rating=models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) 
    reviews=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        return {'rating': self.rating, 'reviews': self.reviews}

class CustomerRating(models.Model):
    customer=models.ForeignKey(Customer, on_delete= models.CASCADE, related_name="customer_rating")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='rating_product')

    seller=models.ForeignKey(Seller, on_delete= models.CASCADE, related_name='seller_rating_customer')
    
    rating=models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) 
    reviews=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reviews

