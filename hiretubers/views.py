from django.core.checks import messages
from django.shortcuts import redirect, render
from .models import Hiretuber

# Create your views here.

def hiretuber(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        tuber_id = request.POST['tuber_id']
        tuber_name = request.POST['tuber_name']
        city = request.POST['city']
        state = request.POST['state']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        email = request.POST['email']

        #Todo : do sanitization

        hiretuber = Hiretuber(first_name=first_name, last_name=last_name, tuber_id=tuber_id, tuber_name=tuber_name, city=city, state=state, phone=phone, messages=messages, user_id=user_id, email=email)
        hiretuber.save()
        messages.success(request, 'Thanks for submitting your query')
        return redirect('youtubers')