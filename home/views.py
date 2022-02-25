from django.shortcuts import render
from product.models import SweetCategory

# Create your views here.
def home(request):
    return render(request, 'base.html')


def navbase(request):
    return render(request, 'navbase.html')


def displaybody(request):
    return render(request, 'displaybody.html')


def shop(request):
    data = SweetCategory.objects.all().order_by('-id')
    return render(request, 'home/shop.html', {'data' : data})


def why(request):
    return render(request, 'home/why.html')
    

def testimonial(request):
    return render(request, 'home/testimonial.html')    


def contact(request):
    return render(request, 'home/contact.html')



