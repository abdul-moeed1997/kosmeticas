from django.contrib import admin
from  .models import Product, Image, Order, OrderUpdate, Contact
# Register your models here.

admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Order)
admin.site.register(OrderUpdate)
admin.site.register(Contact)