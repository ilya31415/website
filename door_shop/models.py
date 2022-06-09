from django.core.validators import RegexValidator
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    price = models.IntegerField()
    image = models.ImageField(upload_to='articles/', null=True, blank=True)

    def display_categories_name(self):
        return ', '.join([category.name for category in self.categories.all()[:3]])

    def __str__(self):
        return self.name


class Order(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=40)
    client = models.ForeignKey(
        'Client',
        related_name='order',
        on_delete=models.CASCADE
    )
    product = models.ManyToManyField(
        Product,
        through='ProductOrder',
        related_name='order'
    )
    order_cost = models.IntegerField()


class ProductOrder(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product'
        )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='order'
    )
    quantity = models.IntegerField()


class Categories(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=40)
    product = models.ManyToManyField(
        Product,
        through='CategoriesProduct',
        related_name='categories'
    )

    def display_products_name(self):
        return ', '.join([products.name for products in self.product.all()[:3]])

    def __str__(self):
        return self.name


class CategoriesProduct(models.Model):
    categories = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE,
        related_name='categories1'

    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='products'

    )


class Client(models.Model):
    name = models.CharField(max_length=30)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=16)

    def __str__(self):
        return self.name
