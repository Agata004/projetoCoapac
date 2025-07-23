from django.shortcuts import render

def index(request):
    return render (request, 'index.html')

def admins(request):
    return render (request, 'admins.html')