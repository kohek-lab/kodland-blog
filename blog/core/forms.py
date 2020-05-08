from django.forms import ModelForm, CharField, Textarea
from .models import Post


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('post_title', 'post_body', 'post_image')
