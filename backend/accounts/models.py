from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """ Model to represent additional information about user """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    bio = models.TextField(
        max_length=2000,
        blank=True,
        default=''
    )
    # we use URL instead of imagefield because we'll use 3rd party img hosting later on
    # https://blog.codeinfuse.com/upload-multiple-files-to-cloudinary-using-react-dropzone-axios-27883c2a5ec6
    avatar = models.URLField(default='', blank=True)
    status = models.CharField(max_length=30, default='', blank=True)

    def __str__(self):
        return self.user.username