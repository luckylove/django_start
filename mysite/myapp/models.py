from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# lets create the post database
# class that inharit from the django models class

# if we use auto_now_add = True in the DateTimeField then we cannot change
# the date

# we can have one to many relations
# between the users and the authors of the post
# for that you are using foreign key and linked it with the user table
# which you will create in future

# on cascade basically set what will happen (means to delete)
# the post when the particular user is deleted accordingly
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    # special method and used to specify what we want to
    # return when we query the database for the output accordingly
    # this function is used to specify the output
    # when we query on the Post model accordingly

    def __str__(self):
        return self.title

