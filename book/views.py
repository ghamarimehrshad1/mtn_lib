from unicodedata import category
from django.db.models import Q
from django.shortcuts import render ,redirect
from book.models import Book,Bookmark,Comment
from author.models import Author
from accounting.models import CustomUser
from extra.models import Publisher,Category,Like
from django.core.paginator import Paginator
from book.forms import CommentForm,BookForm,AdvanceSearch
from django.contrib.auth.models import User



def book_list(request):
    books=Book.objects.all()
    p=Paginator(Book.objects.all(),1)
    page=request.GET.get('page')
    pag_Book=p.get_page(page)
    
    
    context={'books':books,'pag_book': pag_Book}
    return render (request,'book/book_list.html',context)



def book_list_1author(request,author):
    author_obj = Author.objects.get(name=author)
    books=Book.objects.filter(author=author_obj)
    context={'books':books }
    return render (request,'book/book_list_1author.html',context)



def book_list_1publisher(request,publisher):
    publisher_obj=Publisher.objects.get(name=publisher)
    books=Book.objects.filter(Publisher=publisher_obj)
    context={'books':books}
    return render (request,'book/book_list_1publisher.html',context)



def book_list_1category(request,category):
    category_obj=Category.objects.get(name=category)
    books=Book.objects.filter(category=category_obj)
    context={'books':books}
    return render (request,'book/book_list_1category.html',context)



def book_detail(request,pk):
    book_obj=Book.objects.get(id=pk)
    related_book=Book.objects.filter(Publisher=book_obj.Publisher)
    comments=Comment.objects.filter(book=book_obj)
    like_obj=Like.objects.filter(book=book_obj).filter(vote=True).count()
    diss_like_obj=Like.objects.filter(book=book_obj).filter(vote=False).count()
    context={'book':book_obj,'comments':comments,'like':like_obj,'diss_like':diss_like_obj,'whatsapp_url':'','telegram_url':'',
    'related_book':related_book}
    return render (request,'book/book_detail.html',context)



def add_comment(request,u_id,b_id):
    user_obj=User.objects.get(id=u_id)
    custom_user_obj=CustomUser.objects.get(user=user_obj)
    book_obj=Book.objects.get(id=b_id)
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid:
            new_form = form.save(commit=False)
            new_form.user = custom_user_obj
            new_form.book = book_obj
            new_form.save()

            # cd=form.cleaned_data
            # title=cd.get('title')
            # content=cd.get('content')
            # comment=Comment.objects.create(user=custom_user_obj,book=book_obj,title=title,content=content)
            return redirect('book:book_list')

    else:
        form=CommentForm()
        context={'form':form}
        return render(request,'book/add_comment.html',context)



def add_bookmark(request,u_id,b_id):

    user_obj=User.objects.get(id=u_id)
    custom_user_obj=CustomUser.objects.get(user=user_obj)
    book_obj=Book.objects.get(id=b_id)
    bookmark_obj = Bookmark.objects.get(user=custom_user_obj,)
    bookmark_obj.book.add(book_obj)
    bookmark_obj.save()
    return redirect ('book:book_list')
    


def bookmark_list(request,id):
    user_obj=User.objects.get(id=id)
    custom_user_obj=CustomUser.objects.get(user=user_obj)
    bookmark_list_obj=Bookmark.objects.get(user=custom_user_obj)
    context={'bookmark_list':bookmark_list_obj}
    return render (request,'book/bookmark_list.html',context)
    


def delete_from_bookmark(request, bmk_id, b_id):
    bookmark_list_obj=Bookmark.objects.get(id=bmk_id)
    book_obj=Book.objects.get(id=b_id)
    bookmark_list_obj.book.remove(book_obj)
    return redirect ('book:book_list')



def add_book(request,u_id):
    user_obj=User.objects.get(id=u_id)
    custom_user_obj=CustomUser.objects.get(user=user_obj)
    if request.method=='POST':
        form=BookForm(request.POST)
        if form.is_valid():
            new_form=form.save(commit=False)
            new_form.user=custom_user_obj
            form.save()
            return redirect('book:book_list')


    else:
        form=BookForm()
        context={'form':form}
        return render (request,'book/add_book.html',context)



def update_book(request,u_id,b_id):
    book_obj=Book.objects.get(id=b_id)
    user_obj=User.objects.get(id=u_id)
    custom_user_obj=CustomUser.objects.get(user=user_obj)
    if request.method=='POST':
        form=BookForm(request.POST,instance=book_obj)
        if form.is_valid():
            new_form=form.save(commit=False)
            new_form.user=custom_user_obj
            form.save()
            return redirect('book:book_list')


    else:
        form=BookForm(instance=book_obj)
        context={'form':form}
        return render (request,'book/update_book.html',context)



def delete_book(request,b_id):
    book_obj=Book.objects.get(id=b_id)
    book_obj.delete()
    return redirect ('book:book_list')



def search_book(request):
    book_name=request.POST['book_name']
    book_obj=Book.objects.filter(name__icontains=book_name)
    context={'books':book_obj}
    # context={'books':books,'pag_book': pag_Book}
    return render (request,'book/book_list.html',context)
    # return render (request,'book/filter_book.html',context)



def advance_search(request):
    if request.method=='POST':
        form=AdvanceSearch(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            book_name=cd['book_name']
            exact_book_name=cd['exact_book_name']
            author_name=cd['author_name']
            publisher_name=cd['publisher_name']
            # author_obj=Author.objects.get(name=author_name)
            # publisher_obj=Publisher.objects.get(name=publisher_name)
            if exact_book_name==False:
                qexpr=( Q(name__icontains=book_name) )  
                if author_name:
                    qexpr &= Q(author__name=author_name)
                book_obj=Book.objects.filter(qexpr)
                if publisher_name:
                    qexpr &= Q(Publisher__name=publisher_name)
                book_obj=Book.objects.filter(qexpr)
                
            else:
                qexpr=(Q (name=book_name) ) 
                if author_name:
                    qexpr &= Q(author__name=author_name)
                book_obj=Book.objects.filter(qexpr)
                if publisher_name:
                    qexpr &= Q(Publisher__name=publisher_name)
                book_obj=Book.objects.filter(qexpr)                  
            context={'books':book_obj}
            return render (request,'book/advance_search.html',context)
    form=AdvanceSearch()
    context={'form':form}
    return render (request,'book/advance_search_form.html',context)


def related_book(request,pk):
    book_obj=Book.objects.get(id=pk)
    print('############################')
    print(book_obj)
    return render(request,'book/book_detail.html')


