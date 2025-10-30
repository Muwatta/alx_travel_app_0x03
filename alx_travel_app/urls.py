from django.contrib import admin
from django.urls import path
from listings.views import trigger_email

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trigger-email/', trigger_email, name='trigger_email'),
]
