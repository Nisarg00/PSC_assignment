from  django.shortcuts import render
from .models import food_item
from django.conf import settings

# Create your views here.

this_location_restaurants = [
    {
        'Name' : 'riveta',
        'Rcode': 'R01',
        'Rating': 4.3,
    },
    {
        'Name' : 'riveta',
        'Rcode': 'R01',
        'Rating': 4.3,
    },
    {
        'Name' : 'riveta',
        'Rcode': 'R01',
        'Rating': 4.3,
    }
]

def home(request):
    context = {
        'this_location_restaurants': this_location_restaurants
    }
    return render(request,"FUDIEE/home.html",context)

def about(request):
    return render(request,"FUDIEE/about.html",{'title':'about Fudiee'})


def index(request):
    items = food_item.objects.all()
    print(settings.BASE_DIR)
    print(settings.MEDIA_ROOT)

    types = ['Drinks','Pizzas']
    return render(request,"FUDIEE/index.html",{'items': items,'types':types})
