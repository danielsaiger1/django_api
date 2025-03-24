import requests
from django.shortcuts import render
from rest_framework.authtoken.models import Token

def home(request):
    api_url = 'http://127.0.0.1:8000/api/recipe/recipes/'

    token, _ = Token.objects.get_or_create(user=request.user)
    
    headers = {
        'Authorization': f'Token {token.key}'
    }

    res = requests.get(api_url, headers=headers)
    data = res.json() if res.status_code == 200 else {}

    return render(request, 'home.html', {'data': data})
