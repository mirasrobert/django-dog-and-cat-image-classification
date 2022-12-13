from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('check_image/', views.check_image),
    path('output/<str:result>/', views.output),
    path('about/', views.about),
]
