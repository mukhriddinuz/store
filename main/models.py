from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    username = models.CharField(max_length=55, verbose_name='Isim familyasi')
    phone_number = models.CharField(max_length=150, verbose_name='Telefon Raqam', unique=True)

    class Meta:
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Foydalanuvchi'

    def __str__(self):
        return self.username


class Banner(models.Model):
    image = models.ImageField(upload_to='banner_photo/')
    title = models.CharField(max_length=255)
    text = models.TextField()


class Shop_colloection(models.Model):
    image = models.ImageField(upload_to='shop_picture/')
    short_text = models.CharField(max_length=55)



class Products(models.Model):
    image = models.ImageField(upload_to='product_photo/')
    title = models.CharField(max_length=55)
    price = models.IntegerField(default=0)


class Treding_ats(models.Model):
    image = models.ImageField(upload_to='tredign_photo/')
    title = models.CharField(max_length=55)
    name = models.CharField(max_length=100)


class Brand(models.Model):
    image = models.ImageField(upload_to='brand_photo/')



class Contact(models.Model):
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    image = models.ImageField(upload_to='partner_photo/')





