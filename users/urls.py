from django.urls import path
from . import views

urlpatterns = [
    path('reader_signup/',views.ReaderSignUpView.as_view(), name='reader_signup'),
    path('author_signup/',views.AuthorSignUpView.as_view(), name='author_signup'),
    path('validate_email', views.validate_email, name='validate_email'),
    path('verify_otp', views.VerifyOTPView.as_view(), name='verify_otp'),
    path('resend_otp/', views.ResendOTPView.as_view(), name='resend_otp'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('check_password_match/', views.check_password_match, name='check_password_match'),
    path('validate_email/', views.validate_email, name='validate_email'),
]
