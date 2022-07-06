from django.urls import path,include
from book import views

app_name = 'book'
urlpatterns = [
    path('', views.book_list , name='book_list'),
    path('book_detail/<int:pk>/', views.book_detail, name='book-detail'),
    path('book_1author/<str:author>/', views.book_list_1author, name='book_1author'),
    path('book_1category/<str:category>/',views.book_list_1category,name='book_1category'),
    path('book_1publisher/<str:publisher>/',views.book_list_1publisher,name='book_1publisher'),
    path('add_comment/<int:u_id>/<int:b_id>',views.add_comment,name='add_comment'),
    path('bookmark_list/<int:id>',views.bookmark_list,name='bookmark-list'),
    path('delete_from_bookmark/<int:bmk_id>/<int:b_id>',views.delete_from_bookmark,name='delete_from_bookmark'),
    path('add_bookmark/<int:u_id>/<int:b_id>',views.add_bookmark,name='add_bookmark'),
    path('add_book/<int:u_id>',views.add_book,name='add_book'),
    path('update_book/<int:u_id>/<int:b_id>',views.update_book,name='update_book'),
    path('delete_book/<int:b_id>',views.delete_book,name='delete_book'),
    path('search_book/',views.search_book,name='search_book'),
    path('advance_search_form',views.advance_search,name='advance_search_form'),
    path('advance_search',views.advance_search,name='advance_search'),
    path('book_detail/<int:pk>/', views.related_book, name='book-detail'),
]
