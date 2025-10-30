# listings/views.py
from django.http import JsonResponse
from .tasks import send_notification_email

def trigger_email(request):
    send_notification_email.delay(
        "Welcome!",
        "This is a test background email.",
        ["test@example.com"]
    )
    return JsonResponse({"message": "Email sent asynchronously!"})
