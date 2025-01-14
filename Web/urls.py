from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_reports, name='home'),
    path('url/<str:url>/', views.scan_url, name="url"),
    path('ip/<str:ip>/', views.scan_ip, name="ip"),
    path('domain/<str:domain>/', views.scan_domain, name="domain"),
    path('url/<str:hash>/', views.scan_hash, name="hash"),
]