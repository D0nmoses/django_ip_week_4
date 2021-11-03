from django.shortcuts import render, redirect
from .models import Post, Profile, Neighborhood
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm


# Create your views here.

@login_required(login_url='/accounts/login')
def home(request):
    posts = Post.objects.all()

    return render(request, 'all-watch/home.html',{'posts': posts})


@login_required(login_url='/accounts/login')
def new_post(request):
    '''	
    View function to display a form for creating a post to a logged in authenticated user 	
    '''
    current_user = request.user

    current_profile = current_user.profile

    if request.method == 'POST':

        form = NewPostForm(request.POST, request.FILES)

        if form.is_valid:

            post = form.save(commit=False)

            post.user = current_user

            post.profile = current_profile

            post.save()

            return redirect(home, current_user.id)

    else:

        form = NewPostForm()

    title = 'Create Post'

    return render(request,'all-watch/new_post.html', {"form":form})