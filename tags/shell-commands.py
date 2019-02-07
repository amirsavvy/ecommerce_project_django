>>> from tags.models import Tag
>>> q = Tag.objects.all()
>>> q
<QuerySet [<Tag: T-Shirt>, <Tag: t shirt>, <Tag: t_shirt>, <Tag: Red>]>
>>> q.last()
<Tag: Red>
>>> q.last().title
'Red'
>>> q.last().active
True
>>> q.last().all()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Tag' object has no attribute 'all'
>>> test = q.last()
>>> test
<Tag: Red>
>>> test.products
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x0000018C03CF5780>
>>> test.products.all()
<ProductQuerySet [<Product: Shoes>, <Product: T-Shirt>]>
>>> test.products.all().first()
<Product: Shoes>
>>> exit()

(ecommerceEnv) F:\Learning\Python\ecommerce_project>python manage.py shell
Python 3.7.2 (default, Jan  2 2019, 17:07:39) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from products.models import Product
>>> qs = Product.objects.all()
>>> qs
<ProductQuerySet [<Product: Shoes>, <Product: T-Shirt>, <Product: one>, <Product: two>, <Product: My Mobile f>, <Product: My PC F>]>
>>> qs.first()
<Product: Shoes>
>>> tshirt = qs.first(0
... tshirt = qs.first(0
  File "<console>", line 2
    tshirt = qs.first(0
         ^
SyntaxError: invalid syntax
>>> tshirt = qs.first()
>>> tshirt.tag_set
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x00000119298C59E8>
>>> tshirt.tag_set.all()
<QuerySet [<Tag: Red>]>
>>>
