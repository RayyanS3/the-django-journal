from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')

def posts(request):
    pass

def post_page(request):
    pass
