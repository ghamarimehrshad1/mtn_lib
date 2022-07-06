from contextvars import Context
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.core.mail import send_mail
from accounting.form import LoginForm,ProfileForm,ContactUsForm
from book.models import Book
from accounting.models import CustomUser
from loan.models import Debt



def index(request):
    return render(request,'accounting/index.html')



def register(request):

    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            debt_obj = Debt.objects.create(amount=0)
            c_user = CustomUser.objects.create(user=user, debt=debt_obj)
            c_user.save()
            return redirect('accounting:login_user')

    form=UserCreationForm()
    context={'form':form}
    return render(request,'accounting/register.html',context)



def login_user(request):
    
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            username=cd.get('username')
            password=cd.get('password')
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect('book:book_list')
                
            else:
                HttpResponse(' invalid username or password')

    form=LoginForm()
    context={"form":form}
    return render(request,'accounting/login.html',context)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/book')



def user_profile(request,u_id):
    user_obj=User.objects.get(id=u_id)
    c_user_obj=CustomUser.objects.get(user=user_obj)
    context={'user':c_user_obj}
    return render (request,'accounting/profile_user.html',context)


def complete_profile(request,u_id):
    user_obj = User.objects.get(id=u_id)
    c_user_obj = CustomUser.objects.get(user=user_obj)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=c_user_obj,)
        if form.is_valid():
            user_obj = form.save(commit=False)
            cd = form.cleaned_data
            if cd['username']:
                user_obj.user.username = cd['username']
                user_obj.user.save()
            user_obj.save()            
            return redirect('book:book_list')

    form=ProfileForm(instance=c_user_obj)
    context={'form':form}
    return render (request,'accounting/complete_profile.html',context)



def contact_us (request):
    if request.method=='POST':
        form=ContactUsForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            name=cd['name']
            email=cd['email']
            message=cd['message']
            send_mail(name,message,email,['library.django.m@gmail.com'],fail_silently=False,
            auth_user=None, auth_password=None, connection=None, html_message=None,)
            return render (request,'accounting/contact_us.html',{'name':name})


    form=ContactUsForm()
    context={'form':form}
    return render (request,'accounting/contact_us.html',context)


def users_list(request):
    c_user_obj = CustomUser.objects.all()
    context={'users':c_user_obj}
    return render (request,'accounting/users_list.html',context)


def delete_user(request,u_id):
    user_obj = User.objects.get(id=u_id)
    user_obj.delete()
    user_obj.save()
    return redirect('accounting:users_list')



