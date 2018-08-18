from django.db import models

CATEGORY_CHOICES = (
    ('bikes', 'Bikes'),
    ('skateboards', 'Skateboards')
)


class Brand(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=256)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.CharField(max_length=128, choices=CATEGORY_CHOICES)

    def __str__(self):  # use __str__ for python 3.x
        return self.name


class ProductDetailsState(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    num_sellers = models.IntegerField(null=True)
    num_sales = models.IntegerField(null=True)

    def __str__(self):  # must return string!
        return '{} @${}, ({})'.format(self.product, self.price, self.created_at)
