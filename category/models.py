from django.db import models


class Category(models.Model):
    catageory_name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    slug = models.CharField(max_length=100, unique=True)
    cat_image = models.ImageField(upload_to = 'photos/categories', blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name
