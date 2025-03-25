from django.shortcuts import render, redirect
from django.contrib.auth.views import logout

def login_view(request):
    return render(request, 'authentication/login.html')