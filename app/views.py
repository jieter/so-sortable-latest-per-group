from django.db.models import OuterRef, Prefetch, Subquery, Max
from django.shortcuts import render
from django_tables2 import RequestConfig

from .models import Product, ProductDetailsState
from .tables import ProductTable


def table(request):
    data = Product.objects.all().prefetch_related(
        Prefetch(
            'productdetailsstate_set',
            queryset=ProductDetailsState.objects.filter(
                created_at=Subquery(
                    ProductDetailsState.objects.filter(product=OuterRef('product'))
                    .values('product')
                    .annotate(latest=Max('created_at'))
                    .values('latest')[:1]
                )
            ),
            to_attr='current_state'
        )
    )
    table = ProductTable(data)
    RequestConfig(request).configure(table)

    return render(request, 'table.html', {
        'table': table
    })
