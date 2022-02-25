from celery import shared_task
from django.core.mail import message, send_mail
from sweetshop import settings

@shared_task(bind=True)
# def send_mail_after_registration(email):
def send_mail_celery(self, email):
    subject = "Verify email for signup"
    message = f'Hi click on the given link to verify the account http://127.0.0.1:8000/account-verify/'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject = subject, message = message, from_email = from_email, recipient_list = recipient_list)
    return 'mail send successfully using celery'