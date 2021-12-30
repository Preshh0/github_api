from django.shortcuts import render
import requests
# Create your views here.

def github(request):
    user = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' %username
        response = requests.get(url)
        user = response.json()
    else: 
        print("User does not exist.")
    
    return render(request, 'templates/github.html', {'user': user})