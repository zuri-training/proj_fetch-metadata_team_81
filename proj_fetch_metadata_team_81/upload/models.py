from django.utils import timezone
from django.db import models

# Create your models here.


class fileUpload(models.Model):

    date_uploaded=models.DateTimeField(default=timezone.now)
    filename=models.CharField(max_length=100)
    fileurl=models.CharField(max_length=100)
    filetype=models.CharField(max_length=100)
    myfile=models.FileField(upload_to='store/files/')

   # foo = fileUpload.objects.create(file=some_file)
   # foo.attachment.filename

    def __str__(self) -> str:
        return self.name