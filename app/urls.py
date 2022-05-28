
from django.contrib import admin
from django.urls import path
from app.views import home, login, signout, signup, add_todo, delete_todo, change_todo


urlpatterns = [
    path('' , home , name='home' ),
    path('login/' , login, name='login' ),
    path('signup/' , signup ),
    path('logout/' , signout ),
    path('add-todo/' , add_todo ),
    path('delete-todo/<int:id>' , delete_todo ),
    path('change-status/<int:id>/<str:status>' , change_todo ),

]
