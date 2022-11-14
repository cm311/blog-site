from . import views
from . import api
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout_user, name="logout"),
    path('login/', views.login_user, name="login"),
    path('new_post/', views.new_post, name='new_post'),
    path('edit_post/<int:id>', views.edit_post, name="edit_post"),
    path('post_comment/<int:id>', views.post_comment, name="post_comment"),
    path('api/get_recent_articles/<int:page_num>', views.api_get_recent_articles, name="get_recent_articles"),
    path('search/', views.search, name="search"),
]