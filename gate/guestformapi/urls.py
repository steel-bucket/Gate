# guestformapi/urls.py
from django.urls import path
from .views import *

app_name = 'guestformapi'

urlpatterns = [
    path('records/', GuestFormView.as_view(), name='guest_form'),
    path('api/records/', GuestFormAPIView.as_view(), name='guest_form_api'),
    path('success/', success_view, name='guest_form_success'),
]





# from django.urls import path,include
# from . import views
#
# urlpatterns = [
#     path('records', views.GuestFormView.as_view()),
# ]
