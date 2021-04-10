""" Posts views """

from datetime import datetime

# Django 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Models
from posts.models import Post


# Forms
from posts.forms import PostForm

# Create your views here.

@login_required
def create_post(request):
    """ Create a new post view """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            import pdb; pdb.set_trace()
            return redirect('feed')
        
    else:
        form= PostForm()
    
    return render(
        request= request,
        template_name= 'posts/new.html',
        context= {
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )
        

@login_required
def list_posts(request):
    """ List posts """
    posts = Post.objects.all().order_by('-created')
    
    return render(request, 'posts/feed.html', {'posts': posts})
