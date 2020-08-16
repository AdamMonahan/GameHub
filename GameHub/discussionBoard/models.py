from django.db import models
from login.models import User


class PostManager(models.Manager):
    def register(self, post_data):
        return self.create(
            title = post_data['title'],
            content = post_data['content'],
            #author = post_data['user_id'],
        )

    def validate(self, post_data):
        errors = {}
        #title cannot be empty.
        if len(post_data['title']) < 1:
            errors['title'] = "Title cannot be empty."
        #content must contain at least 5 characters.
        if len(post_data['content']) < 5:
            errors['content'] = "Content must contain at lease 5 characters."

        return errors
# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    objects = PostManager()