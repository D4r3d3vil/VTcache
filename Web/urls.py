from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('url/', views.scan_url, name="url"),
    path('ip/<str:ip>/', views.scan_ip, name="ip"),
    path('domain/<str:domain>/', views.scan_domain, name="domain"),
    path('hash/<str:hashStr>/', views.scan_hash, name="hash"),
]