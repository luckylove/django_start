from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# import login required decorator accordingly so that the user cannot go to the profile page unless
# the user is login
from django.contrib.auth.decorators import login_required

# Create your views here.
# we need to create the view for the new app user

    # you need to pass the forms to get the information
    # of the user
    # but it is not very much difficult in django
    # certain forms already exist in the django
    # for creating new users django provide already the usercreation form
    #form = UserCreationForm()
    # now we need to just call the render function
    # which contains request , path and the dictionary of the variable we want to pass to it
    #

    # now we have created form using the about line of code
    # but it is not doing anything
    # to to make it work we need to use the method post
    # so that if the method is post then we just need to create the from
    # and check for the validation else
    # if the method is not post we just simply display the empty form

    # cleaned_data is basically the dictionary which is created when we enter the data
    # to the form accordingly
    # which is now stored in the username


    # now we want to shows the message of success if we recieve the correst data
    # for this django have a build in message libary
    # from django.contrib import messages
    # these messages are called the flash messages
    # and these are one time messages accordingly they only
    # appear only one time after this when we reload they disappear
    # accordingly for it

    # which contains the messages like
    # message.debug
    # message.info
    # message.success
    # message.warning
    # message.error

    # we are using message . success

    # now we just need to redirect to the another
    # page if the username is successfull geted means
    # for login purpose accordingly
    # reverse lookup accordingly is here used




# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # form .save is used to save the details into the database
#             # default database username and password wala
#
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account Created for {username}!')
#             # now this message is created and to make it view we need to
#             # use it in the base template because we want that whenever the flash message is present
#             # we definitely want to display it on the screen accordingly
#             return redirect('blog-home')
#     else:
#         form = UserCreationForm()
#     return render(request,'users/register.html',{'form' : form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # form .save is used to save the details into the database
            # default database username and password wala

            username = form.cleaned_data.get('username')


            # messages.success(request, f'Account Created for {username}!')
            # now this message is created and to make it view we need to
            # use it in the base template because we want that whenever the flash message is present
            # we definitely want to display it on the screen accordingly
            # return redirect('blog-home')


            # now since i have the login page ready so
            # after registration i need to redirect it to the login page and not the blog home page
            # and we should also change the message as well

            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form' : form})


# now lets create the profile which you will be accessing
# once you login into the site
# so lets create it using

@login_required
def profile(request):
    # one model can only be used with one form
    # so we separately create two different forms

    # now to fill the data we use instance= request.user and instance =  request.user.profile
    # if the request is post then only the form is polulated
    # else not so apply the if condition
    # we want to pass the post data into the form
    # also pass the post data request.POST

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance = request.user.profile)
        # now we have validate the data just like above we have did
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # now we have to show to user that their profile is undated successfully
            # just like above
            messages.success(request, f'Your account has been Updated Successfully ')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request,'users/profile.html', context)





