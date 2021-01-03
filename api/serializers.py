from .models import *
from rest_framework import serializers
from rest_example.settings import MEDIA_ROOT
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    # user_name   =   serializers.CharField(max_length=100)
    # profile_pic =   serializers.ImageField(upload_to=MEDIA_ROOT)
     
    class Meta:
        model=Profile
        fields=[
            'id',
            'profile_pic',
            'bio',
            'dob'
        ]

class CommentSerializer(serializers.ModelSerializer):
    commenter = serializers.SerializerMethodField()

    class Meta:
        model   =  Comment
        fields  =  [
              'comment',
              'commenter',  
        ]

    def get_commenter(self,obj):
        return obj.commenter.username    

class BlogSerializer(serializers.ModelSerializer):
    # title       =   serializers.CharField(max_length=50)
    # description =   serializers.TextField()
    #author      =   serializers.ForeignKey
    comments   =    CommentSerializer(many=True)
    class Meta:
        model=Blog
        fields=[
            'title',
            'description',
            'comments'
        ]

class FollowingSerializer(serializers.ModelSerializer):
    username    =   serializers.SerializerMethodField()
    
    def get_username(self,obj):
        followed    =   obj.followed.username
        return followed

    class Meta:
        model = Following
        fields = ["username"]

class FollowerSerializer(serializers.ModelSerializer):
    username    =   serializers.SerializerMethodField()

    def get_username(self,obj):
        follower    =   obj.follower.username
        return follower

    class Meta:
        model = Following
        fields = ["username"]        



class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()    
    followers = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()


    class Meta:
        model=User
        fields=[
            'username',
            'email',
            'profile',
            'blogs',
            'followers',
            'following'
        ]
        

    def get_followers(self,obj):
        return FollowerSerializer(obj.followers.all(), many=True).data    

    def get_following(self, obj):
        return FollowingSerializer(obj.following.all(), many=True).data


