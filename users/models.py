from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # upload profile pic to profile_pics folder(media folder)
    image = models.ImageField(default='default.svg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}'
