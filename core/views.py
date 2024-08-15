from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import SignUpForm, SignInForm

# SignUp View
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Process form data
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            phone = form.cleaned_data['phone']
            
            # Create user and save to database
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = fname
            user.last_name = lname
            user.save()
            return redirect('signin')
        else:
            return render(request, 'auth-sign-up.html', {'form': form})
    else:
        form = SignUpForm()

    return render(request, 'auth-sign-up.html', {'form': form})

# SignIn View
def signin(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Authenticate user
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, "Invalid email or password")
                return render(request, 'auth-sign-in.html', {'form': form})
        else:
            return render(request, 'auth-sign-in.html', {'form': form})
    else:
        form = SignInForm()

    return render(request, 'auth-sign-in.html', {'form': form})

def passwordrec(request):
    return render(request, 'auth-recoverpw.html')

def index(request):
    return render(request, 'index.html')

def add_product(request):
    return render(request, 'page-add-product.html')

def list_product(request):
    return render(request, 'page-list-product.html')

def add_category(request):
    return render(request, 'page-add-category.html')

def list_category(request):
    return render(request, 'page-list-category.html')

def add_purchase(request):
    return render(request, 'page-add-purchase.html')

def list_purchase(request):
    return render(request, 'page-list-purchase.html')

def add_return(request):
    return render(request, 'page-add-return.html')

def list_purchase(request):
    return render(request, 'page-list-purchase.html')

def add_sales(request):
    return render(request, 'page-add-sale.html')

def list_sale(request):
    return render(request, 'page-list-sale.html')

















# from django.shortcuts import render

# # Create your views here.
# def signup(request):
#     if request.method == "POST":
#         fname = request.POST['fname'],
#         lname = request.POST['lname'],
#         email = request.POST['email'],
#         password = request.POST['password'],
#         confirmpassword = request.POST['confirmpassword'],
#         phone = request.POST['phone'],
        
        
#     return render(request, 'auth-sign-up.html')

# def signin(request):
#     return render(request, 'auth-sign-in.html')

# def passwordrec(request):
#     return render(request, 'auth-recoverpw.html')