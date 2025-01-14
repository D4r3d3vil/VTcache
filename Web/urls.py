from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_reports, name='home'),
    path('scan/<str:url>/', views.scan_url, name="scan")
]