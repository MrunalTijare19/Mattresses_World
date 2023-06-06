from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('addproduct/',views.addproduct,name='addproduct'),
    path('<id>/update_product/',views.update_product,name='update_product'),
    path('<id>/delete_product/',views.delete_product,name='delete_product'),
    path('product/',views.product,name='product'),
    path('addemployee/',views.addemployee,name='addemployee'),
    path('employee/',views.employee,name='employee'),
    path('addcustomer/',views.addcustomer,name='addcustomer'),
    path('customer/',views.customer,name='customer'),
    path('createbill/',views.createbill,name='createbill'),
    path('bill/',views.bill,name='bill'),
    path('home/',views.home,name='home'),
   
]






