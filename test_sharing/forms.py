from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget


class PostForm(forms.Form):
    description = forms.CharField(widget=CKEditorWidget())
