from django.urls import path
from .views import *
urlpatterns =[
     path('',main_page,name='main'),
     path('category/<int:pk>/',food_by_category,name='category'),
     path('dish/<int:pk>/',food_detail,name='detail'),
     path('login/',login_user_view,name='login'),
     path('logout/',logout_user_view,name='logout'),
     path('register/',register_user_view,name='register'),
     path('search_food/',search_game,name='search'),
     path('about/',about_site,name='about'),
     path('save_comment/<int:pk>/',save_comment,name='save_comment'),
     path('profile/<int:pk>/',profile_user,name='profile'),
     path('edit_account_profile/',edit_account_profile,name='edit')
]



