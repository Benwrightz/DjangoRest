from rest_framework import serializers
from .models import AppBar, Portell, Landing, Body, Contact, Message

class AppBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppBar
        fields = '__all__'

class PortellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portell
        fields = '__all__'

class LandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Landing
        fields = '__all__'

class BodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'        


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'        
