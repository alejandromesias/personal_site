from django.shortcuts import render

def home_page(request):
    return render(request, 'projects/am_home.html')
