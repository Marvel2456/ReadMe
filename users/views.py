from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils.crypto import get_random_string
from .models import CustomUser
from .forms import AuthorSignUpForm, ReaderSignUpForm
from .emails import send_otp_email
from django.contrib import messages
import random


def validate_email(request):
    email = request.GET.get("email", "")
    if CustomUser.objects.filter(email=email).exists():
        return HttpResponse('<div class="text-red-500">Email already taken</div>', status=400)
    return HttpResponse('<div class="text-green-500">Email is available</div>', status=200)


class AuthorSignUpView(View):
    def get(self, request):
        form = AuthorSignUpForm()
        context = {
            'form': form, 
            'user_type': 'Author'
        }
        return render(request, 'users/author_register.html', context)

    def post(self, request):
        form = AuthorSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_author = True
            user.is_verified = False
            user.save()
            request.session['email'] = user.email
            send_otp_email(user)
            messages.success(request, f'Dear {user.first_name}, please visit your email {user.email} inbox and get your otp code.', extra_tags='alert')
            return redirect('verify_otp')
        
        context = {
            'form': form, 
            'user_type': 'Author'
        }
        return render(request, 'users/author_register.html', context)


class ReaderSignUpView(View):
    def get(self, request):
        form = ReaderSignUpForm()
        context = {
            'form': form, 
            'user_type': 'Reader'
        }
        return render(request, 'users/reader_register.html', context)

    def post(self, request):
        form = ReaderSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_reader = True
            user.is_verified = False 
            user.save()
            request.session['email'] = user.email
            send_otp_email(user)

            messages.success(request, f'Dear {user.first_name}, please visit your email {user.email} inbox and get your otp code.', extra_tags='alert')
            return redirect('verify_otp')
        
        context = {
            'form': form, 
            'user_type': 'Reader'
        }
        return render(request, 'users/reader_register.html', context)



class VerifyOTPView(View):
    def get(self, request):
        """Render the OTP verification page with retained email"""
        email = request.session.get('email', '')
        return render(request, 'users/verify_otp.html', {'email': email})

    def post(self, request):
        """Handle OTP submission"""
        email = request.session.get('email')
        otp = request.POST.get('otp')

        if not email:
            return JsonResponse({"error": "Session expired. Please sign up again."}, status=400)

        try:
            user = CustomUser.objects.get(email=email, otp=otp)
            user.is_verified = True
            user.otp = None
            user.save()

            # Clear session after verification
            del request.session['email']
            
            login(request, user)
            return redirect('index')

        except CustomUser.DoesNotExist:
            return JsonResponse({"error": "Invalid OTP"}, status=400)


class ResendOTPView(View):
    def get(self, request):
        """Resend OTP and redirect to verification page."""
        user = request.user
        if user and not user.is_verified:
            new_otp = random.randint(100000, 999999)
            user.otp = new_otp
            user.save()
            print(f"New OTP for {user.email}: {new_otp}")
            return redirect('verify_otp')
        return redirect('login')


class LoginView(View):
    def get(self, request):
        return render(request, 'users/login.html')
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = CustomUser.objects.filter(email=email).first()
        if user and user.check_password(password):
            login(request, user)
            return redirect('index')
        messages.error(request, 'Invalid email or password')
        return redirect('login')
    
class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect('index')
