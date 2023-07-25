

# Create your views here.
from django.http import HttpResponse

def string_response(request):
    return HttpResponse('this is my first string')

