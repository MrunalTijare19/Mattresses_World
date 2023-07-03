from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    
    def total_price(self):
        return self.price*self.quantity
        
    def __str__(self):
        return self.product_name
    
    def save(self, *args, **kwargs):
        if not self.product_id:
            last_product_id = Product.objects.order_by('-product_id').values_list('product_id', flat=True).first()
            if last_product_id is not None:
                self.product_id = last_product_id + 1
            else:
                self.product_id = 1
        super().save(*args, **kwargs)

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=100)
    employee_mobile_no = models.CharField(max_length=20)
    employee_address = models.TextField()
    employee_salary = models.IntegerField()
    
    
    def __str__(self):
        return self.employee_name
    
    def save(self, *args, **kwargs):
        if not self.employee_id:
            last_employee_id = Employee.objects.order_by('-employee_id').values_list('employee_id', flat=True).first()
            if last_employee_id is not None:
                self.employee_id = last_employee_id + 1
            else:
                self.employee_id = 1
        super().save(*args, **kwargs)

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    customer_mob_no = models.CharField(max_length=10)
    customer_address = models.TextField()
    
    def __str__(self):
        return self.customer_name
    
    def save(self, *args, **kwargs):
        if not self.customer_id:
            last_customer_id = Customer.objects.order_by('-customer_id').values_list('customer_id', flat=True).first()
            if last_customer_id is not None:
                self.customer_id = last_customer_id + 1
            else:
                self.customer_id = 1
        super().save(*args, **kwargs)

class Billing(models.Model):
    bill_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    
    def product_price(self):
        return self.product.price
    
    def bill_amount(self):
        return self.product_price()*self.quantity

    def __str__(self):
        return f"{self.customer} - {self.product} - {self.employee}"
    
    def save(self, *args, **kwargs):
        if not self.bill_id:
            last_bill_id = Billing.objects.order_by('-bill_id').values_list('bill_id', flat=True).first()
            if last_bill_id is not None:
                self.bill_id = last_bill_id + 1
            else:
                self.bill_id = 1
        super().save(*args, **kwargs)

# class Order(models.Model):
#     order_id = models.AutoField(primary_key=True)
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
        
#     def product_price(self):
#         return self.product.price
    
#     def total_price(self):
#         return self.product_price()*self.quantity
    
#     timestamp = models.DateTimeField(auto_now_add=True)






