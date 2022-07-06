from unicodedata import name
from django.core.management.base import BaseCommand

from accounting.models import CustomUser
from author .models import Author
from book.models import Book,Bookmark,Comment
from extra.models import Like,Category,Publisher
from loan.models import Loan,Debt
from django.contrib.auth.models import User

from faker import Faker

fake=Faker()


class Command(BaseCommand):
    help = 'populate data base'

    def handle(self, *args, **kwargs):
        user=User.objects.create(username=fake.name(),password='12345336789asdfG@')
        custom_user_obj=CustomUser.objects.create(age=20,phone_number=123456,gender='M',addres=fake.address(),national_code=1002,user=user)
        pub_obj=Publisher.objects.create(name='novin',address=fake.address())
        category_obj=Category.objects.create(name='joke')
        loan_obj=Loan.objects.create(user=custom_user_obj)
        author_obj=Author.objects.create(name='fhfdhdjkk11k',description='g1njggfjtdjfyxkmgktuk')
        book_obj=Book.objects.create(name='book_32',description='desc_1',traslator='translator_1',Publisher=pub_obj,user=custom_user_obj,loan=loan_obj,
        )
        book_obj.category.add(category_obj)
        book_obj.author.add(author_obj)
        book_obj.save()
        bookmark_obj = Bookmark.objects.create(user=custom_user_obj,)
        bookmark_obj.book.add(book_obj)
        bookmark_obj.save()
        comment_obj = Comment.objects.create(
        user=custom_user_obj,
        book=book_obj,
        title='comm_1',
        content='content_1',)
        #########$##########

        # user2=User.objects.create(username='22gff8lll76yuf',password='123456789asdfg')
        # custom_user_obj2=CustomUser.objects.create(age=20,phone_number=123456,gender='M',addres='dgshdhdh',national_code=1002,user=user2)
        # pub_obj2=Publisher.objects.create(name='2vfsgs11',address='222222dsgdfdhfgfhjghkhhjljkl')
        # category_obj2=Category.objects.create(name='2222fhdhdh235')
        # loan_obj2=Loan.objects.create(user=custom_user_obj2)
        # author_obj2=Author.objects.create(name='2222fhfdhdjkk11k',description='g1njggfjtdjfyxkmgktuk')
        # book_obj2=Book.objects.create(name='book_56',description='desc_1',traslator='traslator_1',Publisher=pub_obj2,user=custom_user_obj2,loan=loan_obj2,
        # )
        # book_obj2.category.add(category_obj2)
        # book_obj2.author.add(author_obj2)
        # book_obj2.save()
        # bookmark_obj2= Bookmark.objects.create(user=custom_user_obj2,)
        # bookmark_obj2.book.add(book_obj2)
        # bookmark_obj2.save()
        # comment_obj2 = Comment.objects.create(
        # user=custom_user_obj2,
        # book=book_obj2,
        # title='comm_2',
        # content='content_2',)
        # ######################

        # user3=User.objects.create(username='33uyi3lgjk1',password='123456789asdfg')
        # custom_user_obj3=CustomUser.objects.create(age=20,phone_number=123456,gender='M',addres='dgshdhdh',national_code=1002,user=user3)
        # pub_obj3=Publisher.objects.create(name='3333vfsgs11',address='33333dsgdfdhfgfhjghkhhjljkl')
        # category_obj3=Category.objects.create(name='3333fhdhdh235')
        # loan_obj3=Loan.objects.create(user=custom_user_obj3)
        # author_obj3=Author.objects.create(name='333fhfdhdjkk11k',description='3333g1njggfjtdjfyxkmgktuk')
        # book_obj3=Book.objects.create(name='book_167',description='desc_1',traslator='translator_1',Publisher=pub_obj3,user=custom_user_obj3,loan=loan_obj3,
        # )
        # book_obj3.category.add(category_obj3)
        # book_obj3.author.add(author_obj3)
        # book_obj3.save()
        # bookmark_obj3= Bookmark.objects.create(user=custom_user_obj3,)
        # bookmark_obj3.book.add(book_obj3)
        # bookmark_obj3.save()
        # comment_obj3 = Comment.objects.create(
        # user=custom_user_obj3,
        # book=book_obj3,
        # title='comm_3',
        # content='content_3',)
        # self.stdout.write("Database has been populated successfully.")











# def add_bookmark(request,u_id,b_id):
    # user_obj=User.objects.get(id=u_id)
    # custom_user_obj=CustomUser.objects.get(user=user_obj)
    # book_obj=Book.objects.get(id=b_id)
    # bookmark_obj = Bookmark.objects.create(user=custom_user_obj,)
    # bookmark_obj.book.add(book_obj)
    # bookmark_obj.save()
    # return redirect ('book_list')