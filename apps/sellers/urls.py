from django.urls import path

from apps.sellers.views import SellerView, ProductBySellerView, SellerProductView

urlpatterns = [
    path("", SellerView.as_view()),
    path("products/", ProductBySellerView.as_view()),
    path("products/<slug:slug>/", SellerProductView.as_view()),
]