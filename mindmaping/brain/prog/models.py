from django.db import models
from django.contrib.auth.models import User
class UserProfileInfo(models.Model):
        user = models.OneToOneField(User,on_delete=models.CASCADE)
        portfolio_site = models.URLField(blank=True)
        profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    #class Restaurant(models.Model):
    # numberofrestaurant = models.IntegerField(blank=True, null=True)
    #  location = models.IntegerField(blank=True, null=True)
    #  city=models.TextField(blank=True, null=True )
    #   discountcode = models.IntegerField(blank=True, null=True)
    #   address = models.TextField(blank=True, null=True)
    #   inf = models.TextField()

    #   def __str__(self):
    #      return self.cname.name



   # class Menu(models.Model):
    #    noofdishe = models.IntegerField(blank= True, null= True)
     #   price = models.IntegerField(blank= True, null=True)
      #  description = models.TextField(blank=True, null= True)



       # class Discount(models.Model):
           # offercode = models.TextField(blank=True, null= True)
            #offertnc = models.IntegerField(blank= True, null= True)
            #offeramount = models.IntegerField(blank= True, null= True)

