from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Cart, Order

# Create your views here.

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookstore/book_list.html', {'books': books})

def book_detail(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'bookstore/book_detail.html', {'book': book})

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

def add_to_cart(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.user.is_authenticated:
        cart = Cart.objects.get_or_create(user=request.user)[0]
        cart.items.add(book)
        return redirect('book_list')
    else:
        # Handle anonymous user
        return redirect('login')

def remove_from_cart(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user)
        cart.items.remove(book)
        return redirect('cart')
    else:
        # Handle anonymous user
        return redirect('login')

def checkout(request):
    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user)
        total_price = sum(book.price for book in cart.items.all())
        return render(request, 'bookstore/checkout.html', {'cart': cart, 'total_price': total_price})
    else:
        # Handle anonymous user
        return redirect('login')

