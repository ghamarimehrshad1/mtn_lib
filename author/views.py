from django.shortcuts import render,redirect
from author.models import Author
from author.forms import AuthorForm


def author_list(request):
    author_obj=Author.objects.all()
    context={'authors':author_obj}
    return render (request,'author/author_list.html',context)




def add_author(request): 
    if request.method=='POST':
        form=AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author:author_list')


    else:
        form=AuthorForm()
        context={'form':form}
        return render (request,'author/add_author.html',context)


def update_author(request,a_id):
    category_obj=Author.objects.get(id=a_id)
    if request.method=='POST':
        form=AuthorForm(request.POST,instance=category_obj)
        if form.is_valid(): 
            form.save()
            return redirect('author:author_list')


    else:
        form=AuthorForm(instance=category_obj)
        context={'form':form}
        return render (request,'author/update_author.html',context)


def delete_author(request,a_id):
    category_obj=Author.objects.get(id=a_id)
    category_obj.delete()
    return redirect ('author:author_list')


