from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Message
from .serializers import UserSerializer, MessageSerializer


# API to list all users except the currently authenticated user

class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return User.objects.exclude(id=self.request.user.id)

# API endpoint to get conversation messages and sending new messages

class ConversationAPIView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        other_user_id = self.kwargs.get('user_id')
        other_user = User.objects.get(id=other_user_id)
        return Message.objects.filter(
            sender__in=[self.request.user, other_user],
            recipient__in=[self.request.user, other_user]
        ).order_by('timestamp')
    
    def perform_create(self, serializer):
        other_user_id = self.kwargs.get('user_id')
        other_user = User.objects.get(id=other_user_id)
        serializer.save(sender=self.request.user, recipient=other_user)

# API to get all messages

class MessageListAPIView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Message.objects.filter(
            sender=self.request.user
        ).order_by('-timestamp') 