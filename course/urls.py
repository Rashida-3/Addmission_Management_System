from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home_page, name='home_page'),#login.html for homepage
    path('add_user/', views.add_user, name='add_user'),# add_stud.html
    path('my_course/', views.my_course, name='my_course'),
    path('login/', views.custom_login, name='custom_login'), 
    path('update',  views.update_user, name='update1'),
    # path('update/<int:user_id>/', views.update_user, name='update_user'),
    
    path('logout/', views.logout_user, name='logout'),
    path('navbar_and_sidebar/', views.navbar_and_sidebar, name='navbar_and_sidebar'),
    path('dashboard/', views.search, name='dashboard'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('signup/', views.signup, name='signup'),
    path('update2/<int:pk>/', views.update1, name='update2'),



    
]
