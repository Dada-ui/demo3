from django.urls import path

# importing views from views..py
from home1 import views

urlpatterns = [
	path('geeks_view/', views.geeks_view, name = "template1"),
	path('nav_view/', views.nav_view, name = "template2"),
]