from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Category,Product
from django.core.paginator import Paginator

# Create your views here.\
def index(request):
    category=Category.objects.all().order_by('title')
    cateid=request.GET.get('category')
    if cateid:
        item=Product.objects.filter(category=cateid)
    else:
        item=Product.objects.all()  #access queryset


    paginator=Paginator(item,3)
    num_page=request.GET.get('page')
    user=paginator.get_page(num_page)
    total=user.paginator.num_pages


    context={
        'category':category,
        'item':item,
        'user':user,
        'total':total,
        'num':[i+1 for i in range(total)]
        
        }
    
    return render(request,'main/index.html',context)

def register(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']


        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"your username already exists!!!")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Your email is already exists!!")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.set_password(password)
                user.save()
                return redirect('log_in')
    
        else:
            messages.error(request,"your password is not match!!!")
            return redirect('register')

    return render(request,'main/register.html')

def log_in(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        if not User.objects.filter(username=username).exists():
            messages.error(request,"your username is not in database!!!")
            return redirect('log_in')
        
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request,"password is not valid!!!")
            
    return render(request,'main/login.html')


def log_out(request):
    logout(request)
    return redirect('log_in')

def search_form(request):
    if request.method=='POST':
        searched=request.POST['searched']
        finds=Product.objects.filter(name__icontains=searched)
        nm={
            'searched':searched,
            'finds':finds

        }

        return render(request,'main/search.html',nm)