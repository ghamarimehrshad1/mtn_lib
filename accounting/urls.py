from django.urls import path
from accounting import views


app_name = 'accounting'
urlpatterns = [
    path('register/',views.register,name='register_user'),
    path('login/',views.login_user,name='login_user'),
    path('logout_user/',views.logout_user,name='logout_user'),
    path('',views.index,name='index'),
    path('user_profile/<int:u_id>',views.user_profile,name='user_profile'),
    path('complete_profile/<int:u_id>',views.complete_profile,name='complete_profile'),
    path('contact_us/',views.contact_us,name='contact_us'),
    path('users_list/',views.users_list,name='users_list'),
    path('delete_user/<int:u_id>',views.delete_user,name='delete_user'),
]
