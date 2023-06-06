from django.contrib import admin
from .models import Product,Employee,Customer,Billing

class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_id","product_name","description","price","quantity","total_price"]
    
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["employee_id","employee_name","employee_mobile_no","employee_address","employee_salary"]
    
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["customer_id","customer_name","customer_mob_no","customer_address"]
    
class BillingAdmin(admin.ModelAdmin):
    list_display = ["bill_id","employee","customer","product","product_price","quantity","bill_amount"]
    
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ["order_id","employee","customer","product","product_price","quantity","total_price","timestamp"]


admin.site.register(Product,ProductAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Billing,BillingAdmin)
# admin.site.register(Order,OrderAdmin)
