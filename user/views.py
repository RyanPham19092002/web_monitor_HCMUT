from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,StreamingHttpResponse,HttpRequest
from meetups.models import User, Pass
from django.template import loader
import cv2

# Create your views here.
def login(response):
    if response.method =="POST":
        if response.POST.get("login"):
            username = response.POST.get("username")
            password = response.POST.get("password")
            if username == str(User.objects.get(username=username)):
                print(User.objects.get(username=username))
                for pass_word in User.objects.get(username=username).pass_set.all():
                    if password == str(pass_word):
                        return HttpResponseRedirect("/homepage")
                    else:
                        return HttpResponseRedirect("/login")
            else:
                        return HttpResponseRedirect("/login")
        elif response.POST.get("create"):
            return HttpResponseRedirect("/login/create")
    return render(response,"user/login.html")   
def homepage(response):
    return render(response,"user/Homepage.html")   
def create(response):
    username = ""
    password = ""
    confirm = ""
    email = ""
    if response.method =="POST":
        if response.POST.get("creat account"):
            username = response.POST.get("username")
            password = response.POST.get("password")
            confirm = response.POST.get("confirm")
            email = response.POST.get("email")
            if password == confirm:
                ob = User(username=username)
                ob.save()
                User.objects.get(username=username).pass_set.create(password=password)
                User.objects.get(username=username).email_set.create(email=email)
                return HttpResponseRedirect("/login")
            else:
                return HttpResponseRedirect("/login")
    return render(response,"user/create.html")  