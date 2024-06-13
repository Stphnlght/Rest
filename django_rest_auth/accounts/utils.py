from django.core.mail import EmailMessage
import random
from .models import User, OneTimePassword
from django.conf import settings

def generateOtp():
    otp = ''
    for i in range(5):
        otp += str(random.randint(0,9))
    return otp

def send_code_to_user(email):
    subject = 'One time passcode for email Verification'
    otp_code = generateOtp()
    print(otp_code)
    user = User.objects.get(email=email)
    current_site = 'myAuth.com'
    email_body = f"Hi {user.first_name}, Thanks for signing up on {current_site} please verrify your email with \n the onetime passcode {otp_code}"
    from_email = settings.DEFAULT_FROM_EMAIL

    OneTimePassword.objects.create(user=user, code=otp_code)

    the_email = EmailMessage(subject=subject, body=email_body, from_email=from_email, to=[email])
    the_email.send(fail_silently=True)