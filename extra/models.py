from django.db import models
from accounting.models import CustomUser
from book.models import Book

# book_obj = BookModel.objects.get(id=38)
# book_obj.votes.filter(vote=True).count()
# 
# Like.objects.filter(book=book_obj).filter(vote=True)

class Like(models.Model):
    vote = models.BooleanField(null=True,blank=True)
    user=models.ForeignKey("accounting.CustomUser",on_delete=models.CASCADE)
    book=models.ForeignKey("book.Book",on_delete=models.CASCADE,null=True)
     
    

class Publisher(models.Model):
    name=models.CharField(max_length=25)
    address=models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name=models.CharField(max_length=25)
    def __str__(self):
        return self.name