from django.db import models
from django.contrib.auth.models import User
# this can be used to reduce the size of the image stored as a profile  picture
# pillow library

#form PIL import Image

# Create your models here.
# creating the models for storing the profile picture
# this is going to be one to one model where ever user is having  a profile picture
# and none of the user is their without any profile
# on delete is basically used to indicate what happen with
# the profile when the user is deleted accordingly
# so basically two features onetoonefield and on_delete
# function


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # lets create the Imagefield and set some default pics to display
    # and specify the folder in which the profile image is saving
    image=models.ImageField(default='default.jpg', upload_to='profile.pics')

    # lets define a donder str method to get the output when we call something
    def __str__(self):
        return f'{self.user.username} Profile '

    # we basically want to override the method save so that
    # the size of the image is not stored large




# this particular function is not working because of problem in installing the  ((((( from PIL import Image )))))))

    # def save(self):
    #     super().save()
    #     # first save the original image
    #
    #     # resize the image and specify the size
    #     # lets say 300 px is we select
    #     img = Image.open(self.image.path)
    #     # open the image in the temporary variable
    #     # then check
    #     # set the thrushold
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         # save again at the same path
    #         img.save(self.image.path)
    #
    #


