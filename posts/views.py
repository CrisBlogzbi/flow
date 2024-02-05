from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm, EditCommentForm
from django.utils import timezone  

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', {'posts': posts})

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post, parent_comment=None)
    form = CommentForm()
    reply_form = CommentForm()

    user_is_author = post.is_author(request.user)

    comment_edit_forms = {comment.id: EditCommentForm(instance=comment) for comment in comments}

    if request.method == 'POST':
        if 'parent_comment' in request.POST:
            reply_form = CommentForm(request.POST)
            if reply_form.is_valid():
                reply = reply_form.save(commit=False)
                reply.post = post
                reply.author = request.user
                reply.save()
        elif 'edit_comment_id' in request.POST:
            edit_comment_id = request.POST['edit_comment_id']
            comment_to_edit = get_object_or_404(Comment, pk=edit_comment_id)
            if comment_to_edit.author == request.user:
                comment_edit_forms[comment_to_edit.id] = EditCommentForm(request.POST, instance=comment_to_edit)
                if comment_edit_forms[comment_to_edit.id].is_valid():
                    edited_comment = comment_edit_forms[comment_to_edit.id].save(commit=False)
                    edited_comment.edited_at = timezone.now()
                    edited_comment.save()
            else:
                return render(request, 'error_page.html', {'error_message': 'You are not authorized to edit this comment.'})
        else:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()

    return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments, 'form': form, 'reply_form': reply_form, 'user_is_author': user_is_author, 'comment_edit_forms': comment_edit_forms})




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

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if not post.is_author(request.user):
        return render(request, 'error_page.html', {'error_message': 'You are not authorized to delete this post.'})
    else:
        post.delete()
        return redirect('post_list') 


@login_required
def edit_comment(request, post_id, comment_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == 'POST':
        form = EditCommentForm(request.POST, instance=comment)
        if form.is_valid():
            edited_comment = form.save(commit=False)
            edited_comment.edited_at = timezone.now()
            edited_comment.save()
            return redirect('post_detail', post_id=post_id)
    else:
        form = EditCommentForm(instance=comment)

    return render(request, 'posts/edit_comment.html', {'form': form, 'comment': comment})