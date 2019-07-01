from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    # views.home is basically the function
    # which we want to access
    # blog-home is basically used for reverse backup accordingly
    # this is basically the requeired situations

    # path('', views.home, name='blog-home'),
    # now we want to create a direct view to te PostListView so just override or change this to

    path('', PostListView.as_view(), name='blog-home'),
    # first parameter matches with the url and second parameter matches with the view function and the
    # last parameter is used for reverse backup accordingly
    path('about/', views.about, name='blog-about'),

    # now we are basically creating the view for the individual post
    # and now the url contains some sort of parameters
    # accordingly for it for example if we want to access the first post then
    # post/1 or post/2 etc..

    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),

]