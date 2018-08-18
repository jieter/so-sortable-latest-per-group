from django.db.models import F, Max, OuterRef, Prefetch, Subquery
from django.shortcuts import render
from django_tables2 import RequestConfig

from .models import Product, ProductDetailsState
from .tables import ProductTable


def table(request):
    # this one works only for postgres
    # data = Product.objects.filter(
    #     productdetailsstate__pk__in=ProductDetailsState.objects
    #         .order_by('product_id', '-created_at')
    #         .distinct('product_id')
    # )

    current_state_ids = Product.objects.annotate(current_id=Max('productdetailsstate__id')) \
        .values_list('current_id', flat=True)

    data = Product.objects.filter(productdetailsstate__pk__in=current_state_ids)

    # add annotations to make the table definition cleaner.
    data = data.annotate(
        price=F('productdetailsstate__price'),
        num_sellers=F('productdetailsstate__num_sellers'),
        num_sales=F('productdetailsstate__num_sales')
    )
    table = ProductTable(data)
    RequestConfig(request).configure(table)

    return render(request, 'table.html', {
        'table': table
    })
