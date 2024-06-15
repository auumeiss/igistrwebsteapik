# stats.py
from .models import Order

def orders_count():
    return Order.objects.count()