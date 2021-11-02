from django.urls import path
from . import views 

urlpatterns = [
    #path('', views.base, name="base"),
    path('', views.home, name="home"),
    path('detail/', views.detail, name="detail"),
    path('brands/', views.brand, name="brands"),
    path('vehicle_list/', views.VehicleListView.as_view(), name="vehicle list"),
    path('vehicle/<int:pk>/', views.VehicleView.as_view(), name="vehicle"),
    path('delete_vehicle/<int:pk>/', views.DeleteVehicleView.as_view(), name="delete vehicle"),
    path('create_vehicle/', views.create_vehicle, name="create vehicle"),
    path('update_vehicle/<int:pk>/', views.update_vehicle, name="update vehicle"),
    path('delete/<int:pk>/', views.delete_vehicle, name="delete"),
    
]