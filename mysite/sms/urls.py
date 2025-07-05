from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowDemoPage),           # Handles /
    # path('demo/', views.ShowDemoPage),      # Handles /demo/
    path('login/', views.ShowLoginPage, name='login_page'), 
    path('doLogin', views.doLogin),
    
]
