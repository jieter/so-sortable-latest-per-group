import django_tables2 as tables

from .models import Product


class ProductTable(tables.Table):
    brand = tables.Column(verbose_name='Brand')
    # currentRank = tables.Column()

    price = tables.Column()
    num_sellers = tables.Column()
    num_sales = tables.Column()

    class Meta:
        model = Product
        attrs = {
            'class': 'table'
        }
