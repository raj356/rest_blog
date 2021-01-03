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

def profile(request,username):
    id = User.objects.filter(username = username).first().id
    user    =    requests.get(
        f"http://127.0.0.1:8000/api/user/{id}",
        auth = HTTPBasicAuth('raj', '1234')
    ).json()

    user_profile = requests.get(
        f"http://127.0.0.1:8000/api/profile/{id}",
        auth = HTTPBasicAuth('raj', '1234')
    ).json()

    blogs = []
    for blog in user.get("blogs"):
        request_blog = requests.get(
            f"http://127.0.0.1:8000/api/blog/{id}",
            auth = HTTPBasicAuth('raj', '1234')
        ).json()

        blogs.append(request_blog)

    print(user)
    return render(request, 'profile.html', context = {
        "user": user,
        "blogs": blogs,
        "profile" : user_profile
    }) 

def followers(request, username):
    user_id = User.objects.filter(username=username).first().id
    user_json = requests.get(
        f"http://127.0.0.1:8000/api/user/{user_id}",
        auth = HTTPBasicAuth('raj', '1234')
    ).json()

    followers_list = []
    
    for follower in user_json.get("followers"):
        follower_id = User.objects.filter(username = follower.get("username")).first().id
        follower_json = requests.get(
            f"http://127.0.0.1:8000/api/user/{follower_id}",
            auth = HTTPBasicAuth('raj', '1234')
        ).json()
        print(follower_json)
        followers_list.append(follower_json)

    return render(request, 'followers.html', context = {
        "followers" : followers_list,
        "user" : user_json
    })