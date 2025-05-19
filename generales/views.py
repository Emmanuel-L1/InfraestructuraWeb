from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

def home1(request):
    return HttpResponse("<H1>Home desde Django</H1> \
                        <hr> \
                        <h3>Bienvenido</h3> \
                        <hr>\
                        <p>Estas dentro de mi aplicación, cambeale apa</p>\
                        ")