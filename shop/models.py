from django.db import models

class Product (models.Model):
    male = 'male'
    female = 'female'
    catagory_based_on_gender=[
        (male, 'male'),
        (female,'female')
    ]

    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    gender_catagory = models.CharField(max_length=6, choices=catagory_based_on_gender, default=female)
    catagory = models.CharField(max_length=50)
    sub_catagory = models.CharField(max_length=50)
    price = models.IntegerField(default="0")
    old_price = models.IntegerField(default="0")
    publish_date = models.DateField()
    quantity = models.IntegerField(default="1")
    brand = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Image (models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='shop/images')
    image2 = models.ImageField(upload_to='shop/images')
    image3 = models.ImageField(upload_to='shop/images')

    def __int__(self):
        return self.product

class Order (models.Model):
    order = models.CharField(max_length=5000)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    postcode = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)

class OrderUpdate(models.Model):
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."

class Contact (models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    comment = models.CharField(max_length=5000)

    def __str__(self):
        return self.name