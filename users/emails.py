# import random
# import logging

# from django.core.mail import EmailMessage
# from django.contrib import messages

# logger = logging.getLogger(__name__)

# def generate_otp():
#     """Generate a 6-digit OTP"""
#     return ''.join(random.choices('0123456789', k=6))

# def send_otp_email(request, user):
#     """
#     Send OTP email to the user. 
#     Currently logs OTP to console instead of sending an actual email.
#     """
#     otp = generate_otp()
#     user.otp = otp
#     user.save()

#     # Log OTP to console for now
#     logger.info(f"OTP for {user.email}: {otp}")

#     # Later, replace with actual email sending
#     email = EmailMessage(
#             'Verify Your Email',
#             f'Your OTP is: {otp}',
#             'noreply@yourdomain.com',
#             [user.email],
#             fail_silently=False,
#         )
    
#     if email.send():
#         messages.success(request, f'Dear {user}, please visit your email {user.email} inbox and click on \
#             recieved activation link to confirm and complete the registration. Note: if email is not in your \
#                 inbox, check your spam folder as well.')
#     else:
#         messages.error(request, f'Problem sending email to {user.email}, check that the email is correct.')

#     return otp


import logging
import random

logger = logging.getLogger(__name__)

def generate_otp():
    """Generate a 6-digit OTP"""
    return ''.join(random.choices('0123456789', k=6))

def send_otp_email(user):
    """
    Log OTP instead of sending an actual email.
    """
    otp = generate_otp()
    user.otp = otp
    user.save()

    # Log OTP instead of sending
    logger.info(f"OTP for {user.email}: {otp}")
    print(f"OTP for {user.email}: {otp}")

    return otp  # Return OTP for testing
