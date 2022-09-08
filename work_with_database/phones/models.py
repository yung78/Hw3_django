from django.db import models


class Phone(models.Model):
    #  id = models.BigAutoField(primary_key=True) По умолчанию создает Django
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()

