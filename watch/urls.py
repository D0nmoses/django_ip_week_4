from django.urls import path,re_path
from . import views

urlpatterns = [
    path("",views.home,name='home'),
    re_path(r'^create/post', views.new_post, name="new-post"),
]