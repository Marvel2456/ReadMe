from django.urls import path
from .import views


urlpatterns = [
    path('author_dashboard/', views.authorDashboard, name='author_dashboard'),
    path('books/', views.myBook, name='books'),
]