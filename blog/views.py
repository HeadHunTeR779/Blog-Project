from django.shortcuts import render
from django.models import Post, Comment
from django.utils import timezone
from django.views.generic import (TemplateView, ListView)

# Create your views here.
class AboutView(TemplateView):
    template_name = "blog/about.html"

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"


    #now this ListView "mysteriously" passes all stuff to .htnl in object named posts what if we wanna put some condition
    #as to which objects to give to us? for that we OVERRIDE get_queryset()
    def get_queryset(self):
        return Post.objects.filter(published_date__lte = timezone.now()).orderby("-published_date")
        # default would have been Post.objects.all() notice in orderby I passed a negative sign for DESCENDING
        #else OLDER posts would have come first
