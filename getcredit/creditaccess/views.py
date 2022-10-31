from django.http import HttpResponse

# Create your views here.
def indexPageView(request) :
    return HttpResponse('Welcome to our project')

def aboutPageView(request) :
    return HttpResponse('About Us')

def contactPageView(request) :
    return HttpResponse('Contact Us')