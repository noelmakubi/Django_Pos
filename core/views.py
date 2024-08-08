from django.shortcuts import render

# Create your views here.
def signup(request):
    if request.method == "POST":
        fname = request.POST['fname'],
        lname = request.POST['lname'],
        email = request.POST['email'],
        password = request.POST['password'],
        confirmpassword = request.POST['confirmpassword'],
        phone = request.POST['phone'],
        
        
    return render(request, 'auth-sign-up.html')

def signin(request):
    return render(request, 'auth-sign-in.html')

def passwordrec(request):
    return render(request, 'auth-recoverpw.html')