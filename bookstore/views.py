from django.shortcuts import render
from .models import Book, Cart, Order

# Create your views here.

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookstore/book_list.html', {'books': books})

def cart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.get_or_create(user=request.user)[0]
        return render(request, 'bookstore/cart.html', {'cart': cart})
    else:
        return render(request, 'bookstore/cart.html')

def order_history(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user)
        return render(request, 'bookstore/order_history.html', {'orders': orders})
    else:
        return render(request, 'bookstore/order_history.html')
