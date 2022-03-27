from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView

from posts.models import BlogPost


class BlogHome(ListView):
    model = BlogPost
    context_object_name = 'posts'

    def get_queryset(self):
        """
        overload the get_queryset method to determine if user is logged in
        :return: queryset of posts or queryset of posts with published status
        """
        queryset = super().get_queryset()
        # Verify if the admin user is logged in, if so, show published and non-published posts
        if self.request.user.is_authenticated:
            return queryset
        # filter only published posts for non-authenticated users
        return queryset.filter(published=True)


class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = 'posts/blogpost_create.html'
    fields = ['title', 'content', ]


class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = 'posts/blogpost_edit.html'
    fields = ['title', 'content', 'published', ]


class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name =  'post'

