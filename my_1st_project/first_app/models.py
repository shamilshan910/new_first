from django.db import models

# Create your models here.
class tab1(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='image_upload')
    discr=models.TextField()
    def __str__(self):
      return self.name
class tab2(models.Model):
    name2=models.CharField(max_length=250)
    img2=models.ImageField(upload_to='image_upload2')
    discr2=models.TextField()
    def __str__(self):
      return self.name2