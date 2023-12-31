from django.db import models
from django.contrib.auth.models import User


class Avatar(models.Model):
   image = models.ImageField(upload_to="avatar")
   user = models.ForeignKey(User, on_delete= models.CASCADE)
   
   def __str__(self):
      return f"{self.user} [{self.image}]"

