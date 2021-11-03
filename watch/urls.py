from django.urls import path,re_path
from . import views

urlpatterns = [
    path("",views.home,name='home'),
    re_path(r'^create/post', views.new_post, name="new-post"),
    re_path(r'^profile/(\d+)', views.profile, name="profile"),
    path("business",views.business, name="business"),
    path("business/search_results", views.search_results, name="search_results"),
]