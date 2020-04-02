from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class Post(models.Model):
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    description = RichTextField(null=True,blank=True)

    def __str__(self):
        return f'{self.description}'
