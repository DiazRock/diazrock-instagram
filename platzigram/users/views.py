""" Users views  """

#Django
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.views.generic import DetailView, FormView, UpdateView

#Exceptions
from django.db.utils import IntegrityError

#Models
from django.contrib.auth.models import User
from users.models import Profile
from posts.models import Post

#Forms
from users.forms import ProfileForm, SignupForm

# Create your views here.


def follow_unfollow_profile(request):
    if request.method == "POST":
        logged_user = Profile.objects.get(user = request.user)
        user_id = request.POST.get('profile_id')
        obj = Profile.objects.get(id= user_id)
        if obj in logged_user.user.following.all():
            logged_user.user.following.remove(obj)
        else:
            logged_user.user.following.add(obj)
        
        return redirect(request.META.get('HTTP_REFERER'))    
    
    return redirect('users:detail')


class UserDetailView(LoginRequiredMixin, DetailView):
    """ User detail view """
    
    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'
    
    def get_context_data(self, **kwargs):
        """ Add user's posts to context """
        context = super().get_context_data(**kwargs)
        user= self.get_object()
        logged_user = Profile.objects.get(user = self.request.user)
        context['posts'] = Post.objects.filter(user= user).order_by('-created')
        context['follow'] = [user == p.user for p in logged_user.user.following.all()] != []
        return context


class SignupView(FormView):
    """Users sign up view."""

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile view."""

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        """Return user's profile."""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})


class LoginView(auth_views.LoginView):
    """ Login """
    template_name = 'users/login.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""
    template_name = 'users/logged_out.html'


    
