from django.shortcuts import render, get_object_or_404, redirect  #(instead of redirect u may use HttpResponseRedirect If you want :)
from django.utils import timezone
from django.models import Post, Comment
from blog.forms import PostForm, CommentForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required #this decorator ONLY for functions !!
from django.contrib.auth.mixins import LoginRequiredMixin #use this Mix-in in classes
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

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
    redirect_field_name = "blog/post_form.html"
    form_class = PostForm  #Remember this guy passes its own object named form which has trivial stuff if you wanna send your own form then OVERRIDE
    context_object_name = "form"  #now it sends PostForm in object name of form

    model = Post
    fields = "__all__"
    template_name = "blog/create_post.html"


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "/login/"  #In case the person is not logged where should they go?
    redirect_field_name = "blog/post_detail.html"
    form_class = PostForm  #Remember this guy passes its own object named form which has trivial stuff if you wanna send your own form then OVERRIDE
    context_object_name = "form"  #now it sends PostForm in object name of form

    model = Post
    fields = ["author","title","text"]
    template_name = "blog/create_post.html"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/login/"  #In case the person is not logged where should they go?
    redirect_field_name = "blog/post_detail.html"
    model = Post
    success_url = reverse_lazy("blog:post_list")
    template_name = "school_delete.html"
    context_object_name = "school"


class DraftListView(LoginRequiredMixin, ListView):
    login_url = "/login/"  #In case the person is not logged where should they go?
    redirect_field_name = "blog/post_detail.html"
    model = Post
    template_name = "blog/post_draft_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.object.filter(published_date__isnull = True).orderby('-create_date')



########################################
########################################

@login_required
def comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
        return render(request, 'blog/comment_form.html', {"form":form})


@login_required   #Decorators are love <3
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()  #I have a built-in function
    return redirect('post_detail', pk=comment.post.pk)  #alt is HttpResponseRedirect(reverse()) this is amazing LOL
