from django import template
from posts.forms import EditCommentForm 

register = template.Library()

from typing import Dict

@register.filter
def get_comment_form(comment_edit_forms: Dict[int, EditCommentForm], comment_id: int) -> EditCommentForm:
    return comment_edit_forms[comment_id]