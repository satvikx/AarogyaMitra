from django.shortcuts import render, redirect
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from decouple import config

# from django.contrib import auth
# from django.contrib.auth.models import User
from .models import Chat

from django.utils import timezone
from gradio_client import Client

# HF_TOKEN = config('SECRET_KEY')

def ask_ai(message):
    client = Client("https://givyboy-mental-health-chatbot.hf.space/--replicas/04p3w/")
    result = client.predict(
            message,	# str  in 'Message' Textbox component
            api_name="/chat"
    )
    return result


# Create your views here.
# @csrf_exempt
def chatbot(request):
    chats = Chat.objects.all()

    if request.method == 'POST':
        message = request.POST.get('message')
        print(message)
        # response = "This is my response"
        # print(response)
        response = ask_ai(message)
        # response = response.replace('\n','<br />\n')


        chat = Chat(message=message, response=response, created_at=timezone.now())
        chat.save()
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html', {'chats': chats})

'''
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('chatbot')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return redirect('chatbot')
            except:
                error_message = 'Error creating account'
                return render(request, 'register.html', {'error_message': error_message})
        else:
            error_message = 'Password dont match'
            return render(request, 'register.html', {'error_message': error_message})
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

'''