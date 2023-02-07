from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    img=models.ImageField(upload_to='User/')
    mobile=models.CharField(max_length=50)
    pwd = models.CharField(max_length=400)
    date=models.DateTimeField( auto_now=True,)
   
