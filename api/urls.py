from django.urls import path,include
from api.views import *

urlpatterns=[
    path('blogs/',blogs, name = "blogs"),
    path('profile/<str:username>/', profile, name = "profile"),
    path('followers/<str:username>/', followers, name = "show-followers")
]