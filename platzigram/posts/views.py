"""Posts views."""

# Django
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView

# Forms
from posts.forms import PostForm

# Models
from posts.models import Post
from users.models import Profile

class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 30
    context_object_name = 'posts'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        if not 'username' in self.kwargs:
            return qs
        following_users= [user for user in self.request.user.following.all()]
        
        posts= [ post for u in following_users for post in Profile.objects.get(user = u.user).post_set.all() ]

        return posts
        

class PostDetailView(LoginRequiredMixin, DetailView):
    """Return post detail."""

    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'posts'


def execute_like(request, pk):
    if request.method == "POST":
        likes_connected = get_object_or_404(Post, id= pk)
        context = {
            'post_is_liked': likes_connected.likes.filter(id=request.user.id).exists()
        }
        if not context['post_is_liked']:
            likes_connected.likes.add(request.user)
        else:
            likes_connected.likes.remove(request.user)

        context['post_is_liked'] = not context['post_is_liked']
        context['number_of_likes'] = likes_connected.likes.all().count()
        
        return redirect(request.META.get('HTTP_REFERER'), **context)    
    
    return redirect('posts:detail')
    

class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post."""

    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        context['likes'] = 0
        return context
