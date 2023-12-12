from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('address', views.CustomerAddressViewSet, basename="address")
router.register('productrating', views.ProductRatingViewSet)
router.register('customerrating', views.CustomerRatingViewSet)

urlpatterns = [
    # URLs pour les vendeurs
    path('sellers/', views.SellersListView.as_view(), name='sellers-list'),
    path('seller/<int:pk>/', views.SellerDetailView.as_view(), name='seller-detail'),

    # URLs pour les robes
    path('dresses/', views.DressesListView.as_view(), name='dresses-list'),
    path('dress/<int:pk>/', views.DressDetailView.as_view(), name='dress-detail'),

    # URLs pour les catégories de produits
    path('categories/', views.ProductCategoriesListView.as_view(), name='product-categories-list'),
    path('category/<int:pk>/', views.ProductCategoryDetailView.as_view(), name='product-category-detail'),

    # URLs pour les chaussures
    path('shoes/', views.ShoesListView.as_view(), name='shoes-list'),
    path('shoe/<int:pk>/', views.ShoeDetailView.as_view(), name='shoe-detail'),

    # URLs pour les accessoires
    path('accessories/', views.AccessoriesListView.as_view(), name='accessories-list'),
    path('accessory/<int:pk>/', views.AccessoryDetailView.as_view(), name='accessory-detail'),

    # URLs pour les clients
    path('customers/', views.CustomersListView.as_view(), name='customers-list'),
    path('customer/<int:pk>/', views.CustomerDetailView.as_view(), name='customer-detail'),

    # URLs pour les commandes
    path('orders/', views.OrdersListView.as_view(), name='orders-list'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),

    # URL pour lister les articles de commande
    path('order-items/', views.OrderItemsListView.as_view(), name='order-items-list'),
]

urlpatterns += router.urls