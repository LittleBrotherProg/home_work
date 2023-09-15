from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    filter_objects = request.GET.get("sort")
    if filter_objects == "min_price":
        phone_objects = Phone.objects.all().order_by('price')
    elif filter_objects == "max_price":
        phone_objects = Phone.objects.all().order_by('-price')
    elif filter_objects == "name":
        phone_objects = Phone.objects.all().order_by('name')
    else:
        phone_objects = Phone.objects.all()
    template = 'catalog.html'
    phones = [
                {
                    "name": phone.name,
                    "price": phone.price,
                    "image": phone.image,
                    "release_date": phone.release_date,
                    "lte_exists": phone.lte_exists,
                    "slug": phone.slug
               } 
               for phone in phone_objects
            ]
    context = {
                "phones": phones
              }
    return render(request, template, context)


def show_product(request, slug):
    phone_object = Phone.objects.filter(slug = slug)[0]
    phone = {
                "name": phone_object.name,
                "price": phone_object.price,
                "image": phone_object.image,
                "release_date": phone_object.release_date,
                "lte_exists": phone_object.lte_exists,
                "slug": phone_object.slug

            }
    template = 'product.html'
    context = {"phone":phone}
    return render(request, template, context)
