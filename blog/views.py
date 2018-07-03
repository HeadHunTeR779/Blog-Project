from django.shortcuts import render
from django.models import Post, Comment
from blog.forms import PostForm, CommentForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required #this decorator ONLY for functions !!
from django.contrib.auth.mixins import LoginRequiredMixin #use this Mix-in in classes
from django.views.generic import TemplateView, ListView, DetailView, CreateView

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

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post_detail"


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = "/login/"  #In case the person is not logged where should they go?
    redirect_field_name = "blog/post_detail.html"
    form_class = PostForm  #Remember this guy passes its own object named form which has trivial stuff if you wanna send your own form then OVERRIDE
    context_object_name = "form"  #now it sends PostForm in object name of form

    model = Post
    template_name = "blog/create_post.html"
