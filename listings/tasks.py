from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_booking_confirmation_email(to_email, booking_details):
    subject = "Your Booking Confirmation"
    message = f"Hello,\n\nYour booking has been confirmed!\n\nDetails:\n{booking_details}\n\nThank you for choosing ALX Travel."
    email_from = settings.DEFAULT_FROM_EMAIL

    send_mail(subject, message, email_from, [to_email])
    return "Email sent successfully!"
