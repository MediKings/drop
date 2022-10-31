from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='Catégorie')
    subCategory = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, related_name='Sous_catégorie')
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='img/article/')
    image2 = models.ImageField(upload_to='img/article/', null=True, blank=True)
    image3 = models.ImageField(upload_to='img/article/', null=True, blank=True)
    image4 = models.ImageField(upload_to='img/article/', null=True, blank=True)
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    image = models.ImageField(upload_to='img/order/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    adress = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.name} {self.quantity}'
