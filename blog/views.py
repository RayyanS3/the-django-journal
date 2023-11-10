from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')

def posts(request):
    return render(request, 'all-posts.html')

def post_page(request):
    pass
