from django.shortcuts import render
from .models import Post, Profile, Neighborhood

# Create your views here.
def home(request):
    posts = Post.objects.all()

    return render(request, 'all-watch/home.html',{'posts': posts})