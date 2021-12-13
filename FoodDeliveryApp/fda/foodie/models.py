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

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    phone = models.IntegerField()
    email = models.EmailField(max_length=90)
    address = models.CharField(max_length=200)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zip_code = models.IntegerField()

    def __str__(self):
        return str(self.order_id)