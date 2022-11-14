from django.urls import path
from .views import home, post, about, contact

urlpatterns = [
    path('', home, name="home"),
    path('post/<int:id>', post, name="post"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
]
