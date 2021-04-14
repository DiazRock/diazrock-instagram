""" Users URLs. """

#Django
from django.urls import path
from django.views.generic import TemplateView

#Views
from users import views


urlpatterns = [
    
    
    # Management
    path(
        route ='login/', 
        view= views.LoginView.as_view(), 
        name= 'login'),
    path(
        route= 'logout/', 
        view= views.LoginView.as_view(), 
        name= 'logout'),
    path(
        route= 'signup/', 
        view= views.SignupView.as_view(), 
        name= 'signup'),
    path(
        route='me/profile/', 
        view= views.UpdateProfileView.as_view(), 
        name='update_profile'),
    path (
        'switch_follow/',
        views.follow_unfollow_profile,
        name= 'follow_unfollow_view'
    ),
    
    #Post
    path(
        route = '<str:username>/',
        view= views.UserDetailView.as_view(),
        name= 'detail'
    )
]