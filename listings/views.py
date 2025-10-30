from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Listings App — Django is running successfully!")
