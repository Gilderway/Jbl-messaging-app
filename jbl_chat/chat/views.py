from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from .models import Message

@login_required
def user_list(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, "chat/user_list.html", {"users": users})

@login_required
def conversation(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    messages = Message.objects.filter(
        sender__in = [request.user, other_user],
        recipient__in = [request.user, other_user],
    ).order_by('timestamp')
    return render(request, "chat/conversation.html", {"messages": messages, "other_user": other_user})

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