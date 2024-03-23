from . import views
from django.urls import path


app_name = 'food'
urlpatterns = [

    # path('', views.index, name='index'),
    path('', views.IndexClassView.as_view(), name='index'),

    # path('<int:item_id>/', views.detail, name='detail'),
    path('<int:pk>/', views.FoodDetailClassView.as_view(), name='detail'),

    # path('add/', views.create_item, name='create_item'),
    path('add/', views.CreateItem.as_view(), name='create_item'),


    path('update/<int:item_id>/', views.update_item, name='update_item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),


    path('hello/', views.hello, name='hello'),


]
