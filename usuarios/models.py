from django.db import models
from django.contrib.auth.models import User

class DatosExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biografia = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatares', blank=True, null=True)
    
    def str(self):
        return self.user.username
    

