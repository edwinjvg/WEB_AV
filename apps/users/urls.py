from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('user_create/', user_create, name = 'user_create'),
    path('user_login/', user_login, name='user_login'),
    path('user_logout/', LogoutView.as_view(template_name="users/logout.html"), name="user_logout"),
    path('user_update/', user_update, name='user_update'),
    path('user_avatar/', user_avatar, name='user_avatar'),
    path('user_list/', user_list, name='user_list'),
    path('user_delete/<id>/', user_delete, name='user_delete'),
]

