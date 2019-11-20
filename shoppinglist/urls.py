from django.urls import path
from .views import ItemList, ItemDeleteView

appname='shoppinglist'
urlpatterns = [
    path('list/', ItemList.as_view(),name='list'),
    path('delete', ItemDeleteView.as_view(),name='delete'),
]