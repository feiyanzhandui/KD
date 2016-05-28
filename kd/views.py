from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from kd.models import Order
from django.shortcuts import get_object_or_404
from random import randint
import datetime

# Create your views here.

def home(request):
    return render(request, 'kd/home.html')

def create(request):
    return render(request, 'kd/create.html')

@csrf_protect
def create_order(request):
    if request.method == "POST":
        id = __generate_order_id()
        while Order.objects.filter(id=id).exists():
            id = __generate_order_id()
        Order.objects.create(id=id,
                create_time=datetime.datetime.now(),
                update_time=datetime.datetime.now(),
                current_status=request.POST['package_current_status'],
                current_location=request.POST['package_current_location'],
                weight=request.POST['package_weight'],
                sender_name=request.POST['sender_name'],
                sender_address=request.POST['sender_address'],
                sender_city=request.POST['sender_city'],
                sender_country=request.POST['sender_country'],
                sender_zip=request.POST['sender_zip'],
                sender_contact=request.POST['sender_contact'],
                receiver_name=request.POST['receiver_name'],
                receiver_address=request.POST['receiver_address'],
                receiver_city=request.POST['receiver_city'],
                receiver_country=request.POST['receiver_country'],
                receiver_zip=request.POST['receiver_zip'],
                receiver_contact=request.POST['receiver_contact']
                )
        
    return render(request, 'kd/create.html', {}) 

# Generate 10 digit random nubmer, return string
def __generate_order_id():
    start = 10 ** 9
    end = (10 ** 10) - 1
    return str(randint(start, end))
