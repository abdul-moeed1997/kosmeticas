from django.shortcuts import render
from django.http import HttpResponse
from math import ceil
from django.core.paginator import Paginator
from .models import Product, Image, Order, OrderUpdate, Contact
import json
import logging

def searchResult(query, item):
    query = query.lower()
    if query in item.name.lower() or query in item.desc.lower() or query in item.catagory.lower() or query in item.sub_catagory.lower() or query in item.gender_catagory.lower() or query in item.brand.lower():
        return True
    else:
       return False

def index(request):
    thank = False
    m_images=[]
    w_images=[]
    m_products=Product.objects.filter(gender_catagory='male')
    w_products=Product.objects.filter(gender_catagory='female')
    for product in m_products:
        i=product.image_set.all()
        m_images.append(i[0])
    for product in w_products:
        i=product.image_set.all()
        w_images.append(i[0])
    if request.method == "POST":
        m_email = request.POST.get('email', '')
        contact1 = Contact(name='subscriber', email=m_email, comment='send me news about new sales')
        contact1.save()
        thank = True
    return render(request, "shop/index.html", {'m_products': m_products, 'm_images': m_images, 'w_products': w_products, 'w_images': w_images, 'Thank': thank})



def search(request):
    query = request.GET.get('search')
    images=[]
    brands = []
    brand_count = []
    catagery = []
    cat_count = []
    temp_products = Product.objects.all()
    products=[item for item in temp_products if searchResult(query,item)]
    if len(products) != 0:
        for product in products:
            i = product.image_set.all()
            images.append(i[0])
        for temp_product in temp_products:
            if temp_product.brand not in brands:
                brand = Product.objects.filter(brand=temp_product.brand)
                brands.append(brand[0].brand)
                brand_count.append(brand.count)
            if temp_product.catagory not in catagery:
                cat = Product.objects.filter(catagory=temp_product.catagory)
                catagery.append(cat[0].catagory)
                cat_count.append(cat.count)

        p_paginator = Paginator(products, 9)
        i_paginator = Paginator(images, 9)
        page = request.GET.get('page')
        products = p_paginator.get_page(page)
        images = i_paginator.get_page(page)
        return render(request, "shop/product.html", {'products': products, 'images': images, 'brands': brands, 'brand_count': brand_count, 'catagery': catagery, 'cat_count': cat_count})
    else:
         return render(request, "shop/404.html")
def products(request):
    images=[]
    brands=[]
    brand_count=[]
    catagery=[]
    cat_count=[]
    products = Product.objects.all()

    for product in products:
        i=product.image_set.all()
        images.append(i[0])
        if product.brand not in brands:
            brand = Product.objects.filter(brand=product.brand)
            brands.append(brand[0].brand)
            brand_count.append(brand.count)
        if product.catagory not in catagery:
            cat = Product.objects.filter(catagory=product.catagory)
            catagery.append(cat[0].catagory)
            cat_count.append(cat.count)

    p_paginator = Paginator(products, 9)
    i_paginator = Paginator(images, 9)
    page = request.GET.get('page')
    products = p_paginator.get_page(page)
    images = i_paginator.get_page(page)

    return render(request, "shop/product.html", {'products': products, 'images': images, 'brands': brands, 'brand_count': brand_count, 'catagery': catagery, 'cat_count': cat_count})

def product_details(request, myid):
    r_images=[]
    product = Product.objects.filter(id=myid)
    images = product[0].image_set.all()
    r_products = Product.objects.filter(brand=product[0].brand)
    for r_product in r_products:
        i = r_product.image_set.all()
        r_images.append(i[0])

    return render(request, "shop/productdetails.html", {'product': product[0], 'image': images[0], 'r_products': r_products, 'r_images': r_images })

def about(request):
    return render(request, "shop/about.html")

def checkout(request):
    thank = False
    id = -1
    if request.method == "POST":
        itemJson = request.POST.get('itemJson', '')
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        email = request.POST.get('email', '')
        adress = request.POST.get('address1', '') + "...." + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('postcode', '')
        phone = request.POST.get('phone', '')
        thank = True
        order = Order(order=itemJson, first_name=fname, last_name=lname, email=email, address=adress, city=city, state=state,
                      postcode=zip_code, phone=phone)
        order.save()
        update = OrderUpdate(order_id=order.id, update_desc="The order has been placed")
        update.save()
        id = order.id

    return render(request, 'shop/checkout.html', {'Thank': thank, 'id': id})

def contact(request):
    if request.method == "POST":
        m_name = request.POST.get('name', '')
        m_email = request.POST.get('email', '')
        m_comment = request.POST.get('comment', '')
        contact1 = Contact(name=m_name, email=m_email, comment=m_comment)
        contact1.save()
        thank = True
        return render(request, 'shop/contact.html', {'Thank': thank})
    return render(request, 'shop/contact.html')

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(id=orderId, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].order], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')
