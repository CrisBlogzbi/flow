from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post, parent_comment=None)
    form = CommentForm()
    reply_form = CommentForm()

    if request.method == 'POST':
        if 'parent_comment' in request.POST:
            reply_form = CommentForm(request.POST)
            if reply_form.is_valid():
                reply = reply_form.save(commit=False)
                reply.post = post
                reply.author = request.user
                reply.save()
        else:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()

    return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments, 'form': form, 'reply_form': reply_form})



@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'posts/post_edit.html', {'form': form})

@login_required
def add_comment(request, post_id, parent_comment_id=None):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, post_id=post_id)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.parent_comment_id = parent_comment_id
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm(post_id=post_id)

    return render(request, 'posts/add_comment.html', {'form': form, 'post': post})
