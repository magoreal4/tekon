from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path('', views.Home.as_view(), name='Home'),
    path('download/pdf/<str:title>/', views.download_pdf, name='download_pdf')
]