# to inharit from the usercreationform
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# the use of this file forms.py is basically to use the usercreationform
# and to add some another features like emailid to make the custom user creation form
# and named as UserRegistrationForm accordingly for it

from .models import Profile
# this is imported for the Profile class(Profile Updation form )




class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # here we will create a model so that whenever some user is entered
    # it will enter the data into the user model accordingly

    # model is basically where we want to store the data
    # fields is basically what fields we want to shown in our page

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# now we will use this form instead of UserCreationForm accordingly




# similarly to the above form we create two forms user update data form
# and user profile updation form accordingly for it
# so now lets start

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
