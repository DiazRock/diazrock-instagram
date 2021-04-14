"""Users models."""

# Django
from django.contrib.auth.models import User
from django.db import models
from posts.models import Post


class FollowerRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    """Profile model.

    Proxy model that extends the base data with other
    information.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    
    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    followers = models.ManyToManyField(User, 
                                       related_name='following', 
                                       blank=True,
                                       through= 'FollowerRelation')


    @property
    def posts_count(self):
        """ Return posts count for profile """
        return Post.objects.filter(user__username = self.user.username).count()
        
    
    def __str__(self):
        """Return username."""
        return self.user.username
