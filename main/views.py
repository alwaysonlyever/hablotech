from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def guides_index(request):
    return render(request, 'main/guides/index.html')


def drone_guide(request):
    return render(request, 'main/guides/drones.html')
