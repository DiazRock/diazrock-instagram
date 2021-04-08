''' Platzigram URLS module '''

from django.http import HttpResponse

from datetime import datetime
import json

def hello_world(request):
    """ Return a greeting """
    return HttpResponse('Oh, hi! Current server time is {now}'.format(
        now= datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
        ))
    
def sorted(request):
    """Sorted."""
    numbers = sorted([int(i) for i in request.GET('numbers').split(',')])
    data = {
        'status': 'ok',
        'numbers': numbers,
        'message': 'Integers sorted successfully.'
    }
    return HttpResponse(json.dump(data, indent = 4), content_type= 'application/json')

def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello {}!, wellcome to Platzigram'.format(name)
    return HttpResponse(message)