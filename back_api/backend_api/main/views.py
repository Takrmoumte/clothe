from rest_framework import generics, viewsets
from . import serializers
from . import models

# Vue pour lister et détailler les vendeurs
class SellersListView(generics.ListAPIView):
    queryset = models.Seller.objects.all()
    serializer_class = serializers.SellersListSerializer

class SellerDetailView(generics.RetrieveAPIView):
    queryset = models.Seller.objects.all()
    serializer_class = serializers.SellerDetailSerializer

# Vue pour lister et détailler les robes
class DressesListView(generics.ListAPIView):
    queryset = models.Robe.objects.all()
    serializer_class = serializers.DressListSerializer

class DressDetailView(generics.RetrieveAPIView):
    queryset = models.Robe.objects.all()
    serializer_class = serializers.DressDetailSerializer

# Vue pour lister et détailler les catégories de produits
class ProductCategoriesListView(generics.CreateAPIView):
    queryset = models.ProductCategory.objects.all()
    serializer_class = serializers.ProductCategorySerializer

class ProductCategoryDetailView(generics.RetrieveAPIView):
    queryset = models.ProductCategory.objects.all()
    serializer_class = serializers.ProductCategoryDetailSerializer

# Vue pour lister et détailler les chaussures
class ShoesListView(generics.ListAPIView):
    queryset = models.Shoe.objects.all()
    serializer_class = serializers.ShoeListSerializer

class ShoeDetailView(generics.RetrieveAPIView):
    queryset = models.Shoe.objects.all()
    serializer_class = serializers.ShoeDetailSerializer

# Vue pour lister et détailler les accessoires
class AccessoriesListView(generics.ListAPIView):
    queryset = models.Accessory.objects.all()
    serializer_class = serializers.AccessoryListSerializer

class AccessoryDetailView(generics.RetrieveAPIView):
    queryset = models.Accessory.objects.all()
    serializer_class = serializers.AccessoryDetailSerializer

# Vue pour lister et détailler les clients
class CustomersListView(generics.ListAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerListSerializer

class CustomerDetailView(generics.RetrieveAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerDetailSerializer

# Vue pour lister et détailler les commandes
class OrdersListView(generics.ListAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderListSerializer

class OrderDetailView(generics.RetrieveAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderDetailSerializer

# Vue pour lister les articles de commande (pas de vue détail nécessaire)
class OrderItemsListView(generics.ListAPIView):
    queryset = models.OrderItems.objects.all()
    serializer_class = serializers.OrderItemSerializer

class CustomerAddressViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CustomerAddressSerializer
    queryset = models.CustomerAddress.objects.all()
    http_method_names = ['get', 'post',"delete", "head"]


class ProductRatingViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProductRatingSerializer
    queryset = models.ProductRating.objects.all()
    http_method_names = ['get', 'post',"delete", "head"]

class CustomerRatingViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CustomerRatingSerializer
    queryset = models.CustomerRating.objects.all()
    http_method_names = ['get', 'post',"delete", "head"]