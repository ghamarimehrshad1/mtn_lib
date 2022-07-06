from multiprocessing import context
from django.shortcuts import render,redirect
from extra.models import Publisher,Category,Like
from extra.forms import PublisherForm,CategoryForm
from book.models import Book
from django.contrib.auth.models import User
from accounting.models import CustomUser


def publisher_list(request):
    publisher_obj=Publisher.objects.all()
    context={'publishers':publisher_obj}
    return render (request,'extra/publisher_list.html',context)



def add_publisher(request): 
    if request.method=='POST':
        form=PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('extra:publisher_list')


    else:
        form=PublisherForm()
        context={'form':form}
        return render (request,'extra/add_publisher.html',context)


def update_publisher(request,p_id):
    pulisher_obj=Publisher.objects.get(id=p_id)
    if request.method=='POST':
        form=PublisherForm(request.POST,instance=pulisher_obj)
        if form.is_valid():
            form.save()
            return redirect('extra:publisher_list')


    else:
        form=PublisherForm(instance=pulisher_obj)
        context={'form':form}
        return render (request,'extra/update_publisher.html',context)


def delete_publisher(request,p_id):
    pulisher_obj=Publisher.objects.get(id=p_id)
    pulisher_obj.delete()
    return redirect ('extra:publisher_list')



def category_list(request):
    category_obj=Category.objects.all()
    context={'categorys':category_obj}
    return render (request,'extra/category_list.html',context)




def add_category(request): 
    if request.method=='POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('extra:category_list')


    else:
        form=CategoryForm()
        context={'form':form}
        return render (request,'extra/add_category.html',context)



def update_category(request,c_id):
    category_obj=Category.objects.get(id=c_id)
    if request.method=='POST':
        form=CategoryForm(request.POST,instance=category_obj)
        if form.is_valid(): 
            form.save()
            return redirect('extra:category_list')


    else:
        form=CategoryForm(instance=category_obj)
        context={'form':form}
        return render (request,'extra/update_category.html',context)


def delete_category(request,c_id):
    category_obj=Category.objects.get(id=c_id)
    category_obj.delete()
    return redirect ('extra:category_list')


def search_category(request):
    category_name=request.POST['category_name']
    category_obj=Category.objects.filter(name__icontains=category_name)
    context={'categorys':category_obj}
    return render (request,'extra/filter_category.html',context)


def search_publisher(request):
    publisher_name=request.POST['publisher_name']
    publisher_obj=Publisher.objects.filter(name__icontains=publisher_name)
    context={'publishers':publisher_obj}
    return render (request,'extra/filter_publisher.html',context)



def like_book(request,u_id,b_id):
    book_obj=Book.objects.get(id=b_id)
    user_obj=User.objects.get(id=u_id)
    custom_user_obj=CustomUser.objects.get(user=user_obj)
    like=Like.objects.filter(vote=True,book=book_obj,user=custom_user_obj).exists()
    if like==False:
        Like.objects.filter(vote=False,book=book_obj,user=custom_user_obj).delete()
        Like.objects.create(vote=True,book=book_obj,user=custom_user_obj)
    return redirect ('book:book_list')



def diss_like_book(request,u_id,b_id):
    book_obj=Book.objects.get(id=b_id)
    user_obj=User.objects.get(id=u_id)
    custom_user_obj=CustomUser.objects.get(user=user_obj)
    diss_like=Like.objects.filter(vote=False,book=book_obj,user=custom_user_obj).exists()
    if diss_like==False:
        Like.objects.filter(vote=True,book=book_obj,user=custom_user_obj).delete()
        Like.objects.create(vote=False,book=book_obj,user=custom_user_obj)
    return redirect ('book:book_list')












