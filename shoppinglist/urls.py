from django.urls import path
from .views import ItemList

appname='shoppinglist'
urlpatterns = [
    path('list/', ItemList.as_view(),name='list'),
]