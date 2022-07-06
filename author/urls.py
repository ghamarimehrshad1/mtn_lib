from django.urls import path,include
from author import views

app_name = 'author'
urlpatterns = [
path('author_list', views.author_list , name='author_list'),
path('add_author',views.add_author,name='add_author'),
path('update_author/<int:a_id>',views.update_author,name='update_author'),
path('delete_author/<int:a_id>',views.delete_author,name='delete_author'),

]