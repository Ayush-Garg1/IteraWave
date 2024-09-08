from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return render(request, "home/home_page.html")

def login(request):
    if request.method == "POST":
        email = request.post.get("")
    return render(request, "home/login.html")



# https://www.geeksforgeeks.org/user-authentication-system-using-django/