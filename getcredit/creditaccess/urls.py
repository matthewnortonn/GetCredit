from django.urls import path
from .views import indexPageView
from .views import aboutPageView
from .views import contactPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("about/", aboutPageView, name="about"),
    path("contact/", contactPageView, name="contact"),
    ]
    

