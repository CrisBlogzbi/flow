from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', 'parent_comment')

    def __init__(self, *args, **kwargs):
        post_id = kwargs.pop('post_id', None)
        super(CommentForm, self).__init__(*args, **kwargs)
        if post_id:
            self.fields['parent_comment'].queryset = Comment.objects.filter(post__id=post_id, parent_comment__isnull=True)

class EditCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {'content': forms.Textarea(attrs={'rows': 4})}

    def __init__(self, *args, **kwargs):
        super(EditCommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].required = False

    def set_comment(self, comment):
        # Set the initial data for the comment content
        self.fields['content'].initial = comment.content

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']