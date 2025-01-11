from django.urls import path
from .import views


urlpatterns = [
    path('', views.Index, name='index'),
    path('load-more/', views.load_more, name='load_more'),
]
