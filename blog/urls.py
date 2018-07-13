from django.conf.urls import url
from . import views

app_name = "blog"

urlpatterns = [
    url(r'^$',views.PostListView.as_view(),name="post_list"), #HOme page
    url(r'^about/$', views.AboutView.as_view(), name="about"),  #This is the index page
    url(r'^post/detail/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name="post_detail"), #DOMAIN/detail/pk/
    url(r'^post/new/$', views.PostCreateView.as_view(), name="post_new"), #DOMAIN/post/new/
    url(r'^post/update/(?P<pk>\d+)/$', views.PostUpdateView.as_view(), name="post_update"),
    url(r'^post/delete/(?P<pk>\d+)/$', views.PostDeleteView.as_view(), name="post_delete"),
    url(r'^draft/$',views.DraftListView.as_view(),name="draft_list"),
    url(r'^post/comment/(?P<pk>\d+)/$', views.get_comment_to_post, name="add_comment_to_post"),
    url(r'^post/comment/approve/(?P<pk>\d+)/$', views.comment_approve, name="comment_approve"),
    url(r'^post/comment/delete/(?P<pk>\d+)/$', view.comment_remove, name="comment_remove"),
    url(r'^post/publish/(?P<pk>\d+)/$', view.post_publish, name="post_publish"),
]
