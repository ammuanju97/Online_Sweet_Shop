from django.shortcuts import render
from product.models import SweetProduct
# Create your views here.
def user_home(request):
    product = SweetProduct.objects.all()
    return render(request, 'sweetuser/userhome.html', {'product' : product})
