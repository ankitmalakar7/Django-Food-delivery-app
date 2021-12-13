from django.shortcuts import render
from django.http import HttpResponse
from .models import Foods, Order
import math as m


# Create your views here.
def index(request):
    allFoods = []
    catz_foods = Foods.objects.values('category', 'id')
    cats = {item['category'] for item in catz_foods}
    for cat in cats:
        foods = Foods.objects.filter(category=cat)
        n = len(foods)
        nSlides = n // 4 + m.ceil((n / 4) - (n // 4))
        allFoods.append([foods, range(1, nSlides), nSlides])
    params = {'allFoods': allFoods}
    return render(request, "foodie/index.html", params)


def view(request, food_id):
    fid = Foods.objects.filter(id=food_id)
    print(fid)
    params = {'fid': fid}
    return render(request, "foodie/view.html", params)


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemJSON', '')
        amount = request.POST.get('amount', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip', '')
        phone = request.POST.get('phone', '')
        order = Order(items_json=items_json, amount=amount, name=name, email=email, address=address, city=city,
                      state=state, zip_code=zip_code, phone=phone)
        order.save()
        thank = True
        id = order.order_id
        return render(request, "foodie/checkout.html", {'thank': thank, 'id': id})
    return render(request, "foodie/checkout.html")
