from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializer
from .tasks import send_booking_confirmation_email

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        booking = serializer.save()
        # Prepare email details
        to_email = booking.user.email if hasattr(booking, 'user') else 'test@example.com'
        booking_details = f"Destination: {booking.destination}, Date: {booking.date}, Price: {booking.price}"
        
        # Send asynchronously
        send_booking_confirmation_email.delay(to_email, booking_details)
