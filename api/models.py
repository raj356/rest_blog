from django.db import models
from rest_example.settings import MEDIA_ROOT
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE,related_name="profile")
    dob         = models.DateField(blank=True,null=True)
    bio         = models.CharField(max_length=240,null=True)
    #user_name   = models.CharField(max_length=100,unique=True,null=False)
    profile_pic = models.ImageField(upload_to=MEDIA_ROOT,null=True)

    def __str__(self):
        return self.user.username

class Blog(models.Model):
    title       = models.CharField(max_length=50,null=True)
    description = models.TextField(null=True)
    author      = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="blogs")    

    def __str__(self):
        return f"{self.title}:{self.description}"

class Following(models.Model):
    follower    =   models.ForeignKey(User,related_name="following",on_delete=models.DO_NOTHING)
    followed    =   models.ForeignKey(User,related_name="followers",on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.follower} follows {self.followed}"

class Comment(models.Model):
    comment      =   models.TextField(null=True)
    commenter    =   models.ForeignKey(User,on_delete=models.DO_NOTHING)         
    post         =   models.ForeignKey(Blog,related_name="comments",on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.comment