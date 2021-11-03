from django.contrib import admin
from .models import  Post, Profile, Neighborhood, Business


admin.site.register(Business)
admin.site.register(Neighborhood)
admin.site.register(Post)
admin.site.register(Profile)

