from django.http import HttpResponse
# Create your views here.


def homepage(request):
    welcome = "Hello World,\n Welcome to Remigius Mgbeme's space."
    return HttpResponse(welcome)