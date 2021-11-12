from django.db import models


# Create your models here.
class Foods(models.Model):
    res_id = models.AutoField
    res_name = models.CharField(max_length=30)
    res_adrs = models.CharField(max_length=50)
    category = models.CharField(max_length=20, default="")
    subcategory = models.CharField(max_length=40, default="")
    price = models.IntegerField()
    desc = models.CharField(max_length=10)
    images = models.ImageField(upload_to="foodie/images", default="")

    def __str__(self):
        return self.res_name
