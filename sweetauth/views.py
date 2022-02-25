from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import SweetUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import uuid
from . models import EmailVerifyToken
from .tasks import send_mail_celery
import threading
from django.core.mail import EmailMessage

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SweetUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            # uid = uuid.uuid4()
            # token_email = EmailVerifyToken(token = uid)
            # token_email.save()
            # send_mail_after_registration(user.email, uid)
            #djngo suing
            #  send_mail_after_registration(user.email) 
            #thread using
            send_mail_after_registration(user.email) 
            #celery uisng         
            # send_mail_celery.delay(user.email)
            messages.success(request, "Your Account created successful, to check your mail to verify the account")
            return redirect('user-signup')
    else:
        form = SweetUserForm()
    return render(request, 'sweetauth/signup.html', {'form' : form})


#Sending email using multithreading
class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)
    def run(self):
        self.email.send(fail_silently=False)
   

def send_mail_after_registration(email):
    subject = "Verify email for signup"
    message = f'Hi click on the given link to verify the account http://127.0.0.1:8000/account-verify/'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    email_obj = EmailMessage(
                    subject,
                    message,                    
                    from_email,
                    recipient_list,
                )
    # send_mail(subject = subject, message = message, from_email = from_email, recipient_list = recipient_list)
# SEND MAIL USING MULTITHREADING
    EmailThread(email_obj).start()

def account_verify(request):
    # pf = EmailVerifyToken.objects.filter(token = token).first()
    # pf.verify = True
    # pf.save()
    messages.success(request, 'your account vverifiyed successfully, you can login')
    return redirect('user-login')


def sweet_user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('userhome')
            else:
                messages.error(request, "invalid username or password")
        else:
            messages.error(request, "invalid username or password")
    form = AuthenticationForm()
    return render(request = request, template_name = "sweetauth/login.html", context = {"login_form" : form})


def user_logout(request):
    logout(request)
    messages.info(request, "You have successfully logged out")
    return redirect('home')
