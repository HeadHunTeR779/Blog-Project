from django.conf.urls import url
from . import views

app_name = "blog"

urlpatterns = [
    url(r'^$',views.PostListView.as_view(),name="post_list"), #HOme page
    url(r'^about/$', views.AboutView.as_view(), name="about"),  #This is the index page
    url(r'^post/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name="post_detail"), #DOMAIN/detail/pk/
    url(r'^post/new/$', views.PostCreateView.as_view(), name="post_new"), #DOMAIN/post/new/
]
