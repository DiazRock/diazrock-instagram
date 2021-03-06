""" Post urls """

#Django
from django.urls import path

#Views
from posts import views

urlpatterns = [
    path(
        route = '', 
        view = views.PostsFeedView.as_view(), 
        name = 'feed'),
    path(
        route = 'posts/followed_by_<str:username>', 
        view = views.PostsFeedView.as_view(), 
        name = 'feed_by_follow'),
    path(
        route ='posts/new/', 
        view = views.CreatePostView.as_view(), 
        name= 'create'
        ),
    path(
        route='posts/<int:pk>/',
        view=views.PostDetailView.as_view(),
        name='detail'
    ),
    path(route = 'posts/<int:pk>/like',
         view= views.execute_like,
         name= 'button_like')
]
