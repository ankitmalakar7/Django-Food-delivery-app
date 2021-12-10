from django.shortcuts import render
from django.http import HttpResponse
from .models import Foods
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
    return render(request, "foodie/checkout.html")