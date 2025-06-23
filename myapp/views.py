from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import json


from django.http import HttpResponseRedirect
from django.utils import translation
from django.conf import settings

def set_language(request):
    user_language = request.GET.get('lang', 'en')  # Default to English
    translation.activate(user_language)
    response = HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    return response

"""
import json
from django.utils.translation import gettext as _
from django.conf import settings
import os

def load_translations(lang_code='en'):
    path=os.path.join(settings.BASE_DIR,'static','translation.json')
    with open(path,'r',encoding='utf-8') as f:
       translations= json.load(f)
    return translations.get(lang_code,translations['en'])

"""


def home(request):
    language = request.session.get('language','en')
    with open('static/translations.json','r',encoding='utf-8') as file:
        translations = json.load(file)
    labels = translations.get(language,{})
    return render(request,'index.html',{'labels':labels})

 
    # if request.method == 'POST':
    #     if not request.user.is_authenticated:
    #         messages.error(request, "Please login or register to upload image.")
    #         return redirect('login_user')

    #     image = request.FILES.get('image')
    #     if image:
    #         #ml prediction logic apply
    #         result = "Sample detection result (e.g., Early Blight)"
    #         return render(request, 'index.html', {'result': result})

    # return render(request, 'index.html')




from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.method == 'POST':
       # firstname = request.POST['firstname']
       # lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirn_password']

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return redirect('register')

        user = User.objects.create_user(
           # first_name=firstname,
            #last_name=lastname,
            username=username,
            email=email,
            password=password
        )
        user.save()
        messages.success(request, 'Registration successful! Please login.')
        return redirect('login_user')
    
    return render(request, 'register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def logout_user(request):
    auth.logout(request)
    return redirect('home')

def set_language(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        request.session['language'] = language
    return redirect(request.META.get('HTTP_REFERER', '/'))