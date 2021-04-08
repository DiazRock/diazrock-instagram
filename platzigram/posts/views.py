""" Posts views """
from datetime import datetime
#Django 
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'name': 'Mont Blac',
        'user': 'Yésica Cortés',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1036'
    },
    {
        'name': 'Via láctea',
        'user': 'C. Vander',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=903'
    },
    {
        'name': 'Nuevo Auditorio',
        'user': 'Thespianartist',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1076'
    }
]

def list_posts(request):
    """ List posts """
    content = []
    for post in posts:
        content.append (
            """
            <p><strong> {name} </strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src="{picture}" /></figure>
            """.format(**post)
        )
    return HttpResponse ( '<br>'.join(content))
