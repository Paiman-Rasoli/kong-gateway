from django.urls import path
from . import views

urlpatterns = [
    path('upload/',views.upload),
    path('retrieve/',views.retrieve),
]