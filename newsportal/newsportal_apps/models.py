from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
#    name = models.CharField(max_length=128, null=True)
#    password = models.CharField(('password'), max_length=128)
#    last_login = models.DateTimeField(('last login'), blank=True, null=True)
    rating = models.IntegerField(default=1)
    
    def update_rating(self):
        self.rating = (self.Post.rating * 3) + (self.Comment.rating)

#    is_active = True

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    
class Post(models.Model):
    name = models.CharField(max_length=128, null=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    password = models.CharField(('password'), max_length=128)
    creatoin_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    category = models.ManyToManyField('Post', through='PostCategory')
    header = models.CharField(max_length=128, null=True)
    text = models.TextField(max_length=1024, null=True)
    rating = models.IntegerField(default=1)
    
    def like(self):
        self.rating += 1
        self.save()
    
    def dislike(self):
        if self.rating > 0:
            self.rating -= 1
            self.save()
        else:
            pass
        
    def preview(self):
        return(str(self.text[0:124]) + '...')
    
class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
class Comment(models.Model):
    comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1024, null=True)
    creatoin_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    rating = models.IntegerField(default=1)
    
    def like(self):
        self.rating += 1
        self.save()
    
    def dislike(self):
        if self.rating > 0:
            self.rating -= 1
            self.save()
        else:
            pass