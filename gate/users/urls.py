from django.urls import path
from .views import *

urlpatterns = [
    path("", home),
    path("logout", logout_view),
    path('staffregister/', register_staff, name='staff_register'),
    path('stafflogin/', login_staff, name='staff_login'),
    path('records/', records, name='records'),
]
