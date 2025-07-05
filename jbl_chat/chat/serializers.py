from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Message

# Serializer for User model (id, username, email, firstname, lastname), User instances to JSON
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class MessageSerializer(serializers.ModelSerializer):
    # user related username
    sender_username = serializers.CharField(source='sender.username', read_only=True)
    recipient_username = serializers.CharField(source='recipient.username', read_only=True)
    
    class Meta:
        model = Message
        fields = ['id', 'sender', 'sender_username', 'recipient', 'recipient_username', 'text', 'timestamp']
        read_only_fields = ['sender', 'timestamp'] 