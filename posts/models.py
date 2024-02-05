from django.db import models
from django.contrib.auth.models import User

# Model representing a post
class Post(models.Model):
    title = models.CharField(max_length=255)  # Title of the post
    content = models.TextField()  # Content of the post
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Author of the post, linked to the User model
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the post was created

    # Method to check if a given user is the author of the post
    def is_author(self, user):
        return self.author == user

# Model representing a comment on a post
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # Post to which the comment belongs
    content = models.TextField()  # Content of the comment
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Author of the comment, linked to the User model
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the comment was created
    edited_at = models.DateTimeField(null=True, blank=True)  # Timestamp for when the comment was last edited (optional)
    parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')  # Parent comment if it's a reply, allowing for nested comments
