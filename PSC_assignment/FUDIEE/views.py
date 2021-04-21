from  django.shortcuts import render
from django.http import HttpResponse

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
    return render(request,"FUDIEE/index.html")
