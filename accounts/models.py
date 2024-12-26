from django.db import models
from django.contrib.auth.models import User
import os

def user_face_image_path(instance, filename):

    return os.path.join('images/faces/', instance.user.username, filename)

class FaceLoginAuth(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    face_login = models.ImageField(upload_to=user_face_image_path)

    def __str__(self):
        return self.user.username
