from django.urls import path,include
from extra import views



app_name = 'extra'
urlpatterns = [
path('publisher_list', views.publisher_list , name='publisher_list'),
path('add_publisher',views.add_publisher,name='add_publisher'),
path('update_publisher/<int:p_id>',views.update_publisher,name='update_publisher'),
path('delete_publisher/<int:p_id>',views.delete_publisher,name='delete_publisher'),
path('category_list', views.category_list , name='category_list'),
path('add_category',views.add_category,name='add_category'),
path('update_category/<int:c_id>',views.update_category,name='update_category'),
path('delete_category/<int:c_id>',views.delete_category,name='delete_category'),
path('like_book/<int:u_id>/<int:b_id>',views.like_book,name='like'),
path('diss_like_book/<int:u_id>/<int:b_id>',views.diss_like_book,name='diss_like'),
path('search_category/',views.search_category,name='search_category'),
path('search_publisher/',views.search_publisher,name='search_publisher'),
]