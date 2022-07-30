from django.db import models

# Create your models here.
class food(models.Model):
    Head= models.CharField(max_length=250)
    image=models.ImageField(upload_to='picture')
    des = models.TextField()



