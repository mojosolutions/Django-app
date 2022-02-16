from django.db import models

# Create your models here.
class contacts(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone=models.CharField(max_length=30)
    concern=models.TextField()
    



#python3 manage.py makemigrations after this
#python3 manage.py migrate  (goes to db and creates query)