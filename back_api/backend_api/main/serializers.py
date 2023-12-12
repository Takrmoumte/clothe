from . import models
from django.contrib.auth.models import User
from rest_framework import serializers

# Serializer pour les utilisateurs
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

# Serializer pour les vendeurs (Liste et Détail)
class SellersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Seller
        fields = ["id", "address"]

class SellerDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = models.Seller
        fields = ["id", "user", "address"]

# Serializer pour les catégories de robes
class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductCategory
        fields = ["id", "title","detail"]
        
class ProductCategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductCategory
        fields = ["id", "title", "detail"]

# Serializer de base pour les produits
class ProductListSerializer(serializers.ModelSerializer):
    is_recent = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()
    class Meta:
        model = models.Product
        fields = ["id", "title", "detail", "price", "category", "seller", "average_rating", "is_recent"]
        abstract = True
    
    def get_average_rating(self, obj):
        ratings = obj.product_ratings.all().values_list('rating', flat=True)
        if ratings:
            return round(sum(ratings) / len(ratings), 1)  
        return 0 
        
    def get_is_recent(self, obj):
        return obj.is_recent()

    




class CustomerDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = models.Customer
        fields = ["id", "user", "address", "mobile"]



class ProductRatingSerializer(serializers.ModelSerializer):
    customer = CustomerDetailSerializer()
    class Meta:
        model = models.ProductRating
        fields = ["id", "customer", "product", "rating", "reviews","add_time"]


class ProductDetailSerializer(serializers.ModelSerializer):
    seller = SellerDetailSerializer()
    category = ProductCategorySerializer()
    product_ratings = ProductRatingSerializer(many=True, read_only=True) 

    class Meta:
        model = models.Product
        fields = ["id", "title", "detail", "price", "category", "seller", "product_ratings"]
        abstract = True


# Serializer pour les robes (Liste et Détail)
class DressListSerializer(ProductListSerializer):
    class Meta(ProductListSerializer.Meta):
        model = models.Robe

class DressDetailSerializer(ProductDetailSerializer):
    class Meta(ProductDetailSerializer.Meta):
        model = models.Robe
        fields = ProductDetailSerializer.Meta.fields + ["width", "height", "size"]

# Serializer pour les chaussures (Liste et Détail)
class ShoeListSerializer(ProductListSerializer):
    class Meta(ProductListSerializer.Meta):
        model = models.Shoe

class ShoeDetailSerializer(ProductDetailSerializer):
    class Meta(ProductDetailSerializer.Meta):
        model = models.Shoe
        fields = ProductDetailSerializer.Meta.fields + ["size"]

# Serializer pour les accessoires (Liste et Détail)
class AccessoryListSerializer(ProductListSerializer):
    class Meta(ProductListSerializer.Meta):
        model = models.Accessory

class AccessoryDetailSerializer(ProductDetailSerializer):
    class Meta(ProductDetailSerializer.Meta):
        model = models.Accessory
        # Ajoutez des champs spécifiques pour les accessoires si nécessaire

# Serializer pour les clients (Liste et Détail)
class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ["id", "address", "mobile"]



# Serializer pour les articles de commande (Un seul type car généralement les détails sont les mêmes)
class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductDetailSerializer()

    class Meta:
        model = models.OrderItems
        fields = ["id", "order", "product", "quantity"]

# Serializer pour les commandes (Liste et Détail)
class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = ["id", "status", "created_at"]

class OrderDetailSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    customer = CustomerDetailSerializer()

    class Meta:
        model = models.Order
        fields = ["id", "customer", "status", "created_at", "note", "items"]

class CustomerAddressSerializer(serializers.ModelSerializer):
    customer = CustomerDetailSerializer()

    class Meta:
        model = models.CustomerAddress
        fields = ["id", "customer", "address", "default_address"]

    


class CustomerRatingSerializer(serializers.ModelSerializer):
    customer = CustomerDetailSerializer(),
    seller = SellerDetailSerializer()

    class Meta:
        model = models.CustomerRating
        fields = ["id", "customer", "product", "seller", "rating", "reviews","add_time"]
    
