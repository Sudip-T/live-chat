from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Thread
from django.db.models import Q

User = get_user_model()


def chat(request):
    current_user = request.user
    context = {
        'threads':Thread.objects.filter(Q(first_person=current_user) | Q(second_person=current_user))
    }
    return render(request, 'chat.html', context)