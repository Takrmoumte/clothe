from django.urls import path
from . import views

urlpatterns = [
    path("vendors/", views.VendorList.as_view(), name="vendors"),
    path("vendor/<int:pk>", views.VendorDetail.as_view(), name="vendorDetail"),
]