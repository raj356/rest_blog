from django.shortcuts import render
from django.contrib.auth.models import User

from .serializers import *
from rest_framework import viewsets
from rest_framework import permissions
import requests
from requests.auth import HTTPBasicAuth
# Create your views here.

class ProfileViewSets(viewsets.ModelViewSet):
    queryset    =   Profile.objects.all()
    serializer_class    =   ProfileSerializer
    permission_classes  =   [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class BlogViewSet(viewsets.ModelViewSet):
    queryset    =   Blog.objects.all()
    serializer_class    =   BlogSerializer
    permission_classes  =   [permissions.IsAuthenticated]    

def blogs(request):
    blogs = requests.get(
        "http://127.0.0.1:8000/api/blog/",
        auth = HTTPBasicAuth('raj', '1234')).json()
    print(blogs)
    return render(request, 'index.html', context = {
        "blogs": blogs
    })

def profile(request,user_name):
    id = Profile.objects.filter(user_name = user_name).first().id
    user    =    requests.get(
        f"http://127.0.0.1:8000/api/profile/{id}",
        auth = HTTPBasicAuth('raj', '1234')
    ).json()

    blogs = []
    for blog in user.get("blog"):
        request_blog = requests.get(
            blog,
            auth = HTTPBasicAuth('raj', '1234')
        ).json()

        blogs.append(request_blog)

    print(user)
    return render(request, 'profile.html', context = {
        "user": user,
        "blogs": blogs
    }) 

    