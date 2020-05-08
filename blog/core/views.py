from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView

from .models import Post
from .forms import PostForm


class IndexView(ListView):
    template_name = 'core/index.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return Post.objects.all()[:10]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['page_title'] = 'Блог'
        context['first_post_first_sentence'] = Post.objects.all()[0].post_body.split(".")[0]
        return context


class CreatePostView(View):
    def get(self, request):
        post_form = PostForm()
        return render(request, 'core/post-add.html', {'post_form': post_form, 'page_title': 'Create new topic'})

    def post(self, request, *args, **kwargs):
        post_form = PostForm(request.POST, request.FILES)

        if post_form.is_valid():
            post_form.save()
            return redirect('core:index')

        return redirect('core:new-post')
