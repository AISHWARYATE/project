from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    is_employee = models.BooleanField('Is employee', default=False)


class trolling(models.Model):
    # start_date=models.DateField()
    # end_date=models.DateField()
    alert=models.CharField(max_length=254)


class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self): #show the actual city name on the dashboard
        return self.name

    class Meta: #show the plural of city as cities instead of citys
        verbose_name_plural = 'cities'

class products(models.Model):
    prod_id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True )
    product_name=models.CharField(max_length=254)
    product_dis=models.CharField(max_length=254)
    product_cost=models.IntegerField()
    product_img=models.FileField(upload_to='images')


class cart(models.Model):
    cart_id = models.AutoField(primary_key = True)
    products_name=models.CharField(max_length=254)
    products_cost=models.IntegerField()
    quantity=models.IntegerField()
    
    
    
    

#  class AddBoat(models.Model):
#     boat_no=models.IntegerField()
#     boat_name=models.CharField(max_length=254)


class boat(models.Model):
    boat_no = models.CharField(max_length = 2000)
    boat_name = models.CharField(max_length = 2000)
    no_of_fishermen = models.IntegerField()
    boat_length = models.CharField(max_length = 2000)
    upload_photo =models.ImageField(upload_to='images')

    def __str__(self):
        return self.boat_name


class fishermen(models.Model):
    fname=models.CharField(max_length = 2000)
    city=models.CharField(max_length = 2000)
    age=models.IntegerField()
    phone=models.IntegerField()


