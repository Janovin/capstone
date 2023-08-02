from django.urls import path
from . import views

# Custom decorator requires specifying app space
app_name = 'user_auth'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.registration_view, name='register'),
    
]
