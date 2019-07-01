from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# lets import the listView
from django.views.generic import ListView, DetailView

# these are basically the function view which we are used to
# display on the web brower
# and also we can include the templete of html using some sort of
# render function
#
#def home(request):
    #return HttpResponse('<h1> My Home Page </h1>')

#def about(request):
 #   return HttpResponse('<h1> My About Page </h1>')

# we cannot create all the html into the httpResponse we just use the template
# pass the parameters to the template and do something something accordingly


# this render function is also using http response
# it contains the parameters and the path to the template accordingly


# now we have used both the template accordingly
# and render function to render these template into our
# django project accordingly


# this is the dummy data which we are supplying to the
# def post function for the display to the view accordingly
# using template inharitance accordingly
# posts =[
#     {
#         'author': 'shubham gupta',
#         'title': 'Blog post',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2018'
#     },
#     {
#         'author': 'something gupta',
#         'title': 'Blog post 2',
#         'content': 'second post2 content',
#         'date_posted': 'August 28, 2018'
#     }
#
# ]



# now we need to pass the actual data from the database
# means Post model accordingly for it

def home(request):
    # lets create a dictionary
    # name that dictionary is context
    # this context is basically used to supply the dummy data
    # now we actually want to enter real data

    # context ={
    #     'posts':posts
    # }



    # now to pass the actual data we use
    context={
        'posts' : Post.objects.all()
    }
    # the third argument of the render function is the dictionary
    # of all the variable that we need to pass to the render function

    return render(request,'myapp/home.html',context)


def about(request):
    return render(request,'myapp/about.html')



# till now we talks about the function based views
# but now we are talking about the class based view
# their are a large no of functionality in these types of views
# lets create a class based view for the posts
# list view
# we want to create

class PostListView(ListView):
    # now we need to set the model on which we apply the query
    model = Post
    # since we have changed the view so we need to save the old template and attach it with this new class based view

    template_name = 'myapp/home.html'   #<app>/<model>_<viewtype>.html
    # we need to change the context because in the original home view we have use posts variable as the context and in the
    # list view by default the name is listview so we need to change that context name so we did something like this

    context_object_name = 'posts'

    # now the ordering is not accordingly to the time so we need to change the order of the posts
    # the date_posted will order it (last is the new ) so we use a -ve sign to reverse the order

    ordering =['-date_posted']
    # so now the newest post is at the top


# the above list view is basically using the function based home view
# now we want to create another class based view which is indipendent

class PostDetailView(DetailView):
    # now we need to set the model on which we apply the query
    model = Post
    # now we will make some template with this naming url
    # so that our view will automatically detects it

    # #<app>/<model>_<viewtype>.html





