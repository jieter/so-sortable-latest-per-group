import django_tables2 as tables

from .models import Product


class ProductTable(tables.Table):
    brand = tables.Column(verbose_name='Brand')
    currentRank = tables.Column()

    price = tables.Column(accessor=tables.A('current_state.0.price'))
    num_sellers = tables.Column(accessor=tables.A('current_state.0.num_sellers'))
    num_sales = tables.Column(accessor=tables.A('current_state.0.num_sales'))

    class Meta:
        model = Product
        attrs = {
            'class': 'table'
        }
