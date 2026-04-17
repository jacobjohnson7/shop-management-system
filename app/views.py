from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from app.models import product,customer,Cart 
from django.contrib.auth import logout as auth_logout
from django.contrib import messages


def home(request):
    return render(request,'home.html')


def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user: 
            return render(request, 'adminhome.html')
        else:
            return HttpResponse("Invalid Credentials")  
    return render(request, 'adminlogin.html')
    


def adminhome(request):
    return render(request,'adminhome.html')


def addproduct(request):
    if request.method == 'POST':
        n = request.POST['product_name']
        p = request.POST['price']
        s = request.POST['stock']
        i = request.FILES['image']

        product.objects.create( product_name=n,price=p,stock=s,image=i)
    return render(request, 'addproduct.html')


def viewproduct(request):
    data = product.objects.all()
    return render(request, 'viewproduct.html', {'key': data})

        

def updateproduct(request, id):
    data = product.objects.get(id=id)

    if request.method == 'POST':
        data.product_name = request.POST['product_name']
        data.price = request.POST['price']
        data.stock = request.POST['stock']
        
        if 'image' in request.FILES:
            data.image = request.FILES['image']

        data.save()
        return redirect('viewproduct')


    return render(request, 'addproduct.html', {'i': data})
    


def deleteproduct(request,id):
    data=product.objects.get(id=id)
    data.delete()
    return redirect('viewproduct')


def logout(request):
    auth_logout(request)
    return redirect('home')


def custregister(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        mobile = request.POST.get('mobile') 
        email = request.POST.get('email') 
        password = request.POST.get('password') 
        
        if customer.objects.filter(email=email).exists():
            return HttpResponse("User already exists")
        
        data=customer(firstname=firstname,mobile=mobile,email=email,password=password)
        data.save()
        return render(request,'custlogin.html')
    return render(request,'custregister.html') 

def custlogin(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        data=customer.objects.get(email__icontains=email)
        if data.password==password:
            request.session['member.id']=data.id
            d = product.objects.all()
            return render(request,'userwelcome.html',{'name':data,'key':d})
        else:
            return HttpResponse("invalid")
    return render(request, 'custlogin.html')

def userwelcome(request):
    data = product.objects.all()   

    user_id = request.session.get('member.id')

    if user_id:
        name = customer.objects.get(id=user_id)
    else:
        return redirect('custlogin')   

    return render(request, 'userwelcome.html', {
        'key': data,
        'name': name
    })


def addtocart(request, id):
    if not request.session.get('member.id'):
        return redirect('custlogin')

    prod = product.objects.get(id=id)
    qty = int(request.POST.get('quantity'))

    if qty <= prod.stock:
        Cart.objects.create(
            product=prod,
            user_id=request.session['member.id'],
            quantity=qty
        )
    else:
        return render(request, 'outofstock.html')
    return redirect('userwelcome')


def cart(request):
    if not request.session.get('member.id'):
        return redirect('custlogin')

    user = customer.objects.get(id=request.session['member.id'])
    cart_items = Cart.objects.filter(user=user)
    total = 0
    for i in cart_items:
        total += i.product.price * i.quantity

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })


def removefromcart(request, id):
    if not request.session.get('member.id'):
        return redirect('custlogin')

    item = Cart.objects.get(id=id)
    item.delete()
    return redirect('cart')


def payment(request):
    if not request.session.get('member.id'):
        return redirect('custlogin')

    user = customer.objects.get(id=request.session['member.id'])
    cart_items = Cart.objects.filter(user=user)
    total = sum(i.product.price * i.quantity for i in cart_items)

    if request.method == "POST":
        for i in cart_items:
            i.product.stock -= i.quantity
            i.product.save()

        cart_items.delete()
        return render(request, 'success.html')
    return render(request, 'payment.html', {'total': total})