from django.shortcuts import render

# Create your views here.


def login_alumno(request):
    return render(request, "login.html")


def forgot_password(request):
    return render(request, "forgot-password.html")


def up_protocol(request):
    return render(request, "up-protocol.html")