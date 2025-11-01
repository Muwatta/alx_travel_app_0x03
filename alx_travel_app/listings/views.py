from django.http import JsonResponse
from .tasks import send_booking_confirmation

def trigger_email(request):
    send_booking_confirmation.delay('testuser@example.com', 'Flight to Abuja on Nov 5')
    return JsonResponse({'message': 'Email task triggered successfully!'})
