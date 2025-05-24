from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def leagues(request):
    return render(request, 'leagues.html')

def matches(request):
    return render(request, 'matches.html')

def players(request):
    return render(request, 'players.html')

def teams(request):
    return render(request, 'teams.html')