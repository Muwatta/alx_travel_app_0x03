from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_booking_confirmation_email(to_email, booking_details):
    subject = "Your Booking Confirmation"
    message = (
        f"Hello,\n\nYour booking has been confirmed!\n\n"
        f"Details:\n{booking_details}\n\n"
        "Thank you for choosing ALX Travel."
    )
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [to_email],
        fail_silently=False,
    )
    return "Email sent successfully!"
