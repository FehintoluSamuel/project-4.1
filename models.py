from django.db import models

# Create your models here.
class Media(models.Model):
    file = models.FileField(upload_to='media_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)




