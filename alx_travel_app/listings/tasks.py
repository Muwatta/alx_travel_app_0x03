from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_booking_confirmation(email, booking_details):
    subject = 'Booking Confirmation'
    message = f"Dear user, your booking was successful!\n\nDetails:\n{booking_details}"
    send_mail(subject, message, 'noreply@alxtravel.com', [email])
    return f"Email sent to {email}"
