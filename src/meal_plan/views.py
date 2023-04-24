from django.shortcuts import render

def home(request):
    return render(request, 'meal_plan/home.html', context={})
