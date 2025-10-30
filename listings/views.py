from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializer
from .tasks import send_booking_confirmation_email

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        booking = serializer.save()
        to_email = getattr(booking.user, 'email', 'test@example.com')
        booking_details = f"Destination: {booking.destination}, Date: {booking.date}, Price: {booking.price}"

        # Trigger Celery task for email notification
        send_booking_confirmation_email.delay(to_email, booking_details)
