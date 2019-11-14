from django.views.generic import ListView
from .models import Item

class ItemList(ListView):
    model = Item