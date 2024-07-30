from django.db import models
from phone_field import PhoneField
# Create your models here.
class TodoModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254)
    roll_num=models.IntegerField()
    father_name = models.CharField(max_length=254)
    mother_name = models.CharField(max_length=254)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    email = models.EmailField(max_length=254)
    address = models.TextField()
    gender = models.CharField(max_length=254)
    father_image = models.ImageField(upload_to='blogs')
    mother_image = models.ImageField(upload_to='blogs')
    student_image = models.ImageField(upload_to='blogs')


