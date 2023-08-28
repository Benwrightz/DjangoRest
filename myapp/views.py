from rest_framework import viewsets
from .models import AppBar, Portell, Landing, Body, Contact, Message
from .serializers import AppBarSerializer, PortellSerializer, LandingSerializer, BodySerializer,ContactSerializer, MessageSerializer
from django.http import HttpResponse


def Home(request):
    return HttpResponse("You shouldn't be here")


class AppBarViewSet(viewsets.ModelViewSet):
    queryset = AppBar.objects.all()
    serializer_class = AppBarSerializer

class PortellViewSet(viewsets.ModelViewSet):
    queryset = Portell.objects.all()
    serializer_class = PortellSerializer

class LandingViewSet(viewsets.ModelViewSet):
    queryset = Landing.objects.all()
    serializer_class = LandingSerializer

class BodyViewSet(viewsets.ModelViewSet):
    queryset = Body.objects.all()
    serializer_class = BodySerializer

 
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer   


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer   
