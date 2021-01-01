from django.urls import path,include
from api.views import blogs, profile

urlpatterns=[
    path('blogs/',blogs),
    path('profile/<str:user_name>', profile)
]