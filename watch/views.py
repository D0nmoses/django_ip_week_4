from django.shortcuts import render, redirect
from .models import Post, Profile, Neighborhood
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist


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

            return redirect(home)

    else:

        form = NewPostForm()

    title = 'Create Post'

    return render(request,'all-watch/new_post.html', {"form":form})

@login_required(login_url='/accounts/login/')
def profile(request,id):
    '''	
    View function to display the profile of the logged in user when they click on the user icon	
    '''
    current_user = request.user

    try:

        single_profile = Profile.objects.get(user=current_user.id)

        title = f'{current_user.username}\'s'

        posts = Post.objects.filter(user=current_user.id)

        return render(request, 'all-watch/my_profile.html', {"title":title,"single_profile":single_profile,"current_user":current_user,"posts":posts})

    except ObjectDoesNotExist:
        raise Http404()