from django.urls import path
from .views import ItemList, ItemAddView, ItemDeleteView

appname='shoppinglist'
urlpatterns = [
    path('list/', ItemList.as_view(),name='list'),
    path('add', ItemAddView.as_view(),name='add'),
    path('delete', ItemDeleteView.as_view(),name='delete'),
]