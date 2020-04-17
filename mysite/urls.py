from django.urls import path
from .import views
app_name = 'mysite'

urlpatterns = [
    path('', views.IndexClassView.as_view(), name='index'),
    path('<int:pk>/', views.MysiteDetail.as_view(), name='detailview'),
    # add item in form
    path('add', views.CreateItem.as_view(), name='create_item'),
    # edit item in form
    path('update/<int:id>/', views.update_item, name='update_item'),
    # delete item
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
]