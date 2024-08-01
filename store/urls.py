from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
  path('', views.store, name='store'),  #this renders the default page when clicked on store option at first 
  path('category/<slug:category_slug>/', views.store, name='products_by_category'),
  path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
  path('search/', views.search, name='search'),


]
