from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowDemoPage),      # Handles /
    path('demo/', views.ShowDemoPage), # Handles /demo/
]
