import time

# start with a clean slate
Brand.objects.all().delete()
Product.objects.all().delete()
ProductDetailsState.objects.all().delete()

c = Brand.objects.create(name='Cannondale')
slate_apex = Product.objects.create(name='Slate apex 1', brand=c, category='bikes')
slate_force = Product.objects.create(name='Slate force 1', brand=c, category='bikes')

ProductDetailsState.objects.create(product=slate_apex, price=2000, num_sales=10, num_sellers=4)
ProductDetailsState.objects.create(product=slate_force, price=3000, num_sales=20, num_sellers=10)

print("sleeping for 2 seconds...")
time.sleep(2)  # wait for two seconds, to let the later ProductDetailsState's have a more recent timestamp

ProductDetailsState.objects.create(product=slate_apex, price=2200, num_sales=8, num_sellers=2)
ProductDetailsState.objects.create(product=slate_force, price=2800, num_sales=6, num_sellers=2)


annotated = Product.objects.all().prefetch_related(
    Prefetch(
        'productdetailsstate_set',
        queryset=ProductDetailsState.objects.filter(
            created_at=Subquery(
                ProductDetailsState.objects.filter(product=OuterRef('product'))
                .values('product')
                .annotate(latest=Max('created_at'))
                .values('latest')[:1]
            )
        )
    )
)

print(annotated)
print(annotated[0].productdetailsstate_set.all())
