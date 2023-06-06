from django.shortcuts import render,redirect,get_object_or_404
from .forms.loginform import LoginForm
from django.contrib.auth import authenticate,login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product, Employee, Customer, Billing
from .forms.addproduct import AddProductForm
from .forms.addemployee import AddEmployeeForm
from .forms.addcustomer import AddCustomerForm
from .forms.bill import CreateBillForm
from django.http import HttpResponse




def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')  
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



def home(request):
    return render(request,'test.html')

@login_required(login_url='login')
def dashboard(request):
    product = Product.objects.all()
    employee = Employee.objects.all()
    customer = Customer.objects.all()
    bill = Billing.objects.all()
    return render(request,'dashboard.html',context={'product':product,'employee':employee, 'customer':customer, 'bill':bill})

@login_required(login_url='login')
def product(request):
    product = Product.objects.all()
    return render(request,'products.html',context={'product':product})

@login_required(login_url='login')
def addproduct(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        description = request.POST['description']
        price = request.POST['price']
        quantity = request.POST['quantity']
        
        data = Product(
            product_name=product_name,
            description=description,
            price=price,
            quantity=quantity
        )
        data.save()
        
        return redirect('product')
        
    else:
        form = AddProductForm()
    
    return render(request,'addproduct.html',{'form': form})

def update_product(request,id):
    context ={}
    return render(request,'updateproduct.html',context)
    


def delete_product(request,id):
    context ={}
    obj = get_object_or_404(Product, id = id)
    if request.method =="POST":
        obj.delete()
        return redirect('product')
    return render(request,'teproduct.html',context)



@login_required(login_url='login')
def employee(request):
    employee = Employee.objects.all()
    return render(request,'employees.html',context={'employee':employee})

@login_required(login_url='login')
def addemployee(request):
    if request.method == 'POST':
        employee_name = request.POST['employee_name']
        employee_mobile_no = request.POST['employee_mobile_no']
        employee_address = request.POST['employee_address']
        employee_salary = request.POST['employee_salary']
        
        data=Employee(
            employee_name=employee_name,
            employee_mobile_no=employee_mobile_no,
            employee_address=employee_address,
            employee_salary=employee_salary
        )
        data.save()
        return redirect('employee')
    else:
        form = AddEmployeeForm()
        
    return render(request,'addemployee.html',{'form':form})

@login_required(login_url='login')
def customer(request):
    customer = Customer.objects.all()
    return render(request,'customers.html',context={'customer':customer})

@login_required(login_url='login')
def addcustomer(request):
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        customer_mob_no = request.POST['customer_mob_no']
        customer_address = request.POST['customer_address']
        
        data = Customer(
            customer_name=customer_name,
            customer_mob_no=customer_mob_no,
            customer_address=customer_address
        )
        data.save()
        return redirect('customer')
    else:
        form = AddCustomerForm()
    return render(request,'addcustomer.html',{'form':form})

@login_required(login_url='login')
def bill(request):
    bill = Billing.objects.all()
    return render(request,'billing.html',context={'bill':bill})

# def createbill(request):
#     if request.method == 'POST':
#         employee = request.POST['employee']
#         customer = request.POST['customer']
#         product = request.POST['product']
#         quantity = request.POST['quantity']
#         bill_amount = request.POST['bill_amount']
        
#         data = Billing(
#             employee=employee,
#             customer=customer,
#             product=product,
#             quantity=quantity,
#             bill_amount=bill_amount
#         )
#         data.save()
#         return redirect('bill')
#     else:
#         form = CreateBillForm()
    
#     return render(request,'createbill.html',{'form':form})

@login_required(login_url='login')
def createbill(request):
    if request.method == 'POST':
        form = CreateBillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bill')
    else:
        form = CreateBillForm()
    
    return render(request, 'createbill.html', {'form': form})



def logout(request):
    auth_logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("login")
