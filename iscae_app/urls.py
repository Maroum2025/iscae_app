from django.urls import path

from iscae_app.views import list_item, say_hello_json,html_page,item_create,item_update,item_delete


urlpatterns = [

   # path('say_hello/', say_hello_json),
    path('html_page/', html_page, name='html_page'),
    path('list_item/', list_item, name='list_item'), 
    path('item_create/', item_create, name='item_create'),
    path('items/update/<int:item_id>/',item_update, name='item_update'),
    path('items/delete/<int:item_id>/',item_delete, name='item_delete'),
]