from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'signin.html')
def signup(request):
    username=request.POST.get("username",'default')
    return HttpResponse("logged in successfully")