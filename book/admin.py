from django.contrib import admin
from book.models import Bookmark,Book,Comment


admin.site.register(Book)
admin.site.register(Bookmark)
admin.site.register(Comment)
