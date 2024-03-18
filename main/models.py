from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=150, verbose_name='Telefon Raqam', null=True, blank=True, unique=True)

    class Meta:
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=255)

    def related_model_count(self):
        return Products.objects.filter(category=self).count()

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='brand_image/')

    def related_model_count(self):
        return Products.objects.filter(brand=self).count()

    def __str__(self):
        return self.name


class Products(models.Model):
    image = models.ImageField(upload_to='product_photo/')
    title = models.CharField(max_length=55)
    price = models.IntegerField(default=0)
    product_info = models.TextField(null=True, blank=True)
    brand = models.ForeignKey(to=Brand, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    is_banner = models.BooleanField(default=False)
    banner_title = models.CharField(max_length=100, null=True, blank=True)
    banner_text = models.CharField(max_length=255, null=True, blank=True)
    shop_collections = models.BooleanField(default=False)
    featured_product = models.BooleanField(default=False)
    is_advert = models.BooleanField(default=False)
    advert_text = models.CharField(max_length=50, null=True, blank=True)
    new_product = models.BooleanField(default=True)


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE)


class Contact(models.Model):
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    image = models.ImageField(upload_to='partner_photo/')

    def __str__(self):
        return self.address


class TotalSum(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    products = models.TextField()
    sub_total = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    tax = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    total_expenses = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user.username} - {self.total_expenses}"

