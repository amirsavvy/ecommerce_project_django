import random
import os
from django.db import models
# For slug
from django.db.models.signals import pre_save, post_save

from products.utils import unique_slug_generator

# get file extension
def get_filename_ext(file_path):
    base_name = os.path.basename(file_path)
    name, ext = os.path.splitext(base_name)
    return name, ext

# get file rename
def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1, 343477347734)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)

# Custom queryset
class ProductQuerySet(models.query.QuerySet):
    def featured(self):
        return self.filter(featured = True)

    def active(self):
        return self.filter(active = True)


# Custom Model Manager
class ProductManager(models.Manager):

    # Override builtin methods

    def get_queryset(self):
        return ProductQuerySet(self.model, using = self._db)

    # def all(self):
    #     self.get_queryset().active()

    def featured(self):
        return self.get_queryset().filter(featured = True)

    def get_by_id(self, id):
        # Product.objects == self.get_queryset()
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None



class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10, default=23)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    slug = models.SlugField(default='amir', unique=True, blank=True)



    objects = ProductManager()

    def get_absolute_url(self):
        return "/products/{slug}/".format(slug=self.slug)


    def __str__(self):
        return self.title



def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)
