from django import forms
from .models import Post, Comment

# Form for creating a new post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')

# Form for adding a new comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', 'parent_comment')

    def __init__(self, *args, **kwargs):
        post_id = kwargs.pop('post_id', None)
        super(CommentForm, self).__init__(*args, **kwargs)
        if post_id:
            # Limit parent_comment choices to top-level comments related to the specified post
            self.fields['parent_comment'].queryset = Comment.objects.filter(post__id=post_id, parent_comment__isnull=True)

# Form for editing an existing comment
class EditCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {'content': forms.Textarea(attrs={'rows': 4})}

    def __init__(self, *args, **kwargs):
        super(EditCommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].required = False

    def set_comment(self, comment):
        # Set initial content for the form based on the existing comment
        self.fields['content'].initial = comment.content

# Form for editing an existing post
class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
