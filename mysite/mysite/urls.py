"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
# this can be used to import the predefined login and logout views

# these two are basically used to import the static file for the profile pics section

from django.conf import settings
from django.conf.urls.static import static



# now we are
urlpatterns = [
    path('admin/', admin.site.urls),
    # this is basically used to tell about the urls.py file we have created
    # if we type something known as blog/ then it will check the url from the urls.py file
    # that i have created so far accordingly
    # it matches the myapp with the starting of the url then after that
    # it move on to the myapp.urls for further matching the content
    # if we are unable to get the required url then we get the 404 error
    path('myapp/',include('myapp.urls')),

    # to map the register page
    # i am directly using the views here
    # unlike the above method where we first create the
    # urls.py file in the own app then use that file in this file
    # so directly including looks like this

    path('register/', user_views.register, name='register'),

    # now lets create the profile view
    path('profile/', user_views.profile, name='profile'),

    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # these are basically the template of login and logout system
    # and where we want to use these template these template name is specified in the as_view function accordingly


]


## for the profile pics section
# we are using the debug mode for more convineance for the development stages
# a little bit more understandable

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)

