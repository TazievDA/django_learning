from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    name = models.CharField(255)
    slug = models.SlugField(unique=True)
    price = models.IntegerField()
    image = models.CharField(255)
    release_date = models.DateTimeField()
    lte_exists = models.BooleanField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)
