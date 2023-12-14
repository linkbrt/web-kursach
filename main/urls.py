from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('faq/', views.faq),
    path('room/', views.room),
    path('room/<int:id>/', views.room_reserv),
]