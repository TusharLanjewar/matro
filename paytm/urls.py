from django.urls import path
from . import views  # Assuming views.py is in the same directory as urls.py

urlpatterns = [
    path('', views.homepage, name='homepage'),  # Map root URL to homepage view
    path('login/', views.loginpage, name='loginpage'),  # Example path for login page
    # Add other paths for different pages as needed
]
