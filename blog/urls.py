from django.conf.urls import url
from . import views

app_name = "blog"

urlpatterns = [
    url(r'^$',views.PostListView.as_view(),name="home"), #HOme page
    url(r'^about/$', views.AboutView.as_view(), name="about"),  #This is the index page
]
