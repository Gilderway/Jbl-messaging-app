from django.urls import path
from . import views
from . import api_views
from django.views.generic.base import RedirectView

urlpatterns = [
    # path('', lambda request: redirect('user_list')),

    path('', RedirectView.as_view(pattern_name='user_list', permanent = False)),
    path('users/', views.user_list, name="user_list"),
    path('chat/<int:user_id>/', views.conversation, name="conversation"),
    path('chat/<int:user_id>/send/', views.send_message, name='send_message'),
    path('chat/<int:user_id>/refresh/', views.refresh_messages, name='refresh_messages'),
    
    # API endpoints
    path('api/users/', api_views.UserListAPIView.as_view(), name='api_users'),
    path('api/chat/<int:user_id>/', api_views.ConversationAPIView.as_view(), name='api_conversation'),
    path('api/messages/', api_views.MessageListAPIView.as_view(), name='api_messages'),
]