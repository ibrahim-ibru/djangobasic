from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from app.models import Customer
# Create your views here.
@login_required(login_url="login")
def home(request):
    return render(request, "home.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        b = Customer.objects.filter(username = username)
        for user in b:
            if user.username==username and user.password==password:
                return redirect(home)
            else :
                return HttpResponse("Invalid Credentials")
    return render(request, "Login.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if password == confirmpassword:
            currentuser = Customer.objects.create(username = username, email = email, password = password)
            currentuser.save()
            return redirect(login)
        else:
            return render(request, 'SignUp.html')
    return render(request, "SignUp.html")


