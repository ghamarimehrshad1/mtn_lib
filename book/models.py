from asyncio.windows_events import NULL
from distutils.command.upload import upload
from email.policy import default
from operator import truediv
from unicodedata import category
from django.db import models



class Book(models.Model):

    name=models.CharField(max_length=75)
    cover=models.ImageField(blank=True,upload_to='cover_book',default="cover_book/default.png")
    created_time=models.DateTimeField(auto_now_add=True)
    description=models.TextField()
    traslator=models.CharField(max_length=100)
    Publisher=models.ForeignKey("extra.Publisher",on_delete=models.CASCADE)
    category=models.ManyToManyField("extra.Category")
    author=models.ManyToManyField("author.Author")
    user=models.ForeignKey("accounting.CustomUser",on_delete=models.CASCADE)
    active=models.BooleanField(null=True,blank=True,default=True)
    loan=models.ForeignKey("loan.Loan",null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class  Bookmark(models.Model):

    user=models.OneToOneField("accounting.CustomUser",on_delete=models.CASCADE)    
    book=models.ManyToManyField('book.Book')    
    create = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} has {self.book.count()}'



class Comment(models.Model):

    user=models.ForeignKey("accounting.CustomUser",on_delete=models.CASCADE)
    book=models.ForeignKey("book.Book",on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    content=models.TextField()
    date_time=models.DateTimeField(auto_now=True)


