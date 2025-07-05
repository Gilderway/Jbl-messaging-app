from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from .models import Message

# Display a list of all users except the currently logged-in user
@login_required
def user_list(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, "chat/user_list.html", {"users": users})

# Receive the other user in the conversation using the provided user_id., Return 404 is the user doesn't exist
@login_required
def conversation(request, user_id):
    other_user = get_object_or_404(User, id=user_id)

    # fetch all messages exchanged between the logged-in user and the other user
    messages = Message.objects.filter(
        sender__in = [request.user, other_user],
        recipient__in = [request.user, other_user],
    ).order_by('timestamp')
    return render(request, "chat/conversation.html", {"messages": messages, "other_user": other_user})

# Handle POST request to send a message to another user
@login_required
def send_message(request, user_id):
    if request.method == "POST":
        other_user = get_object_or_404(User, id=user_id)
        text = request.POST.get("text", "").strip()
        if text:
            Message.objects.create(sender=request.user, recipient = other_user, text=text)
            messages = Message.objects.filter(
                sender__in = [request.user, other_user],
                recipient__in = [request.user, other_user]
            ).order_by('timestamp')
            return render(request, 'chat/partials/message_list.html', {"messages": messages})
        return HttpResponseBadRequest("Empty message")
    return HttpResponseBadRequest("Invalid request method")


# Handle Ajax get request to fetc the latest messages between the logged-in user and another specified user real-time chat updates
@login_required
def refresh_messages(request, user_id):
    """Refresh messages for real-time updates"""
    if request.method == "GET":
        other_user = get_object_or_404(User, id=user_id)
        messages = Message.objects.filter(
            sender__in = [request.user, other_user],
            recipient__in = [request.user, other_user],
        ).order_by('timestamp')
        return render(request, 'chat/partials/message_list.html', {"messages": messages})
    return HttpResponseBadRequest("Invalid request method")