from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = ('Categories')
        ordering = ('name',)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product' , on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to = 'images/%Y-%m-%d.jpg', blank= True, null=True)
    slug = models.SlugField(max_length=255)
    price = models.IntegerField()
    in_stock = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = ('Products')
        ordering = ('date_created',)

    def __str__(self):
        return self.name
