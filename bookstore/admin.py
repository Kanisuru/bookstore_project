from django.contrib import admin
from .models import Book, Cart, Order

# Register your models here.

admin.site.register(Book)
admin.site.register(Cart)
admin.site.register(Order)
