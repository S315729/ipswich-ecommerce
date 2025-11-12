from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from cart.models import Cart


@login_required
def create_order(request):
    """Create a new order from the cart"""
    cart = get_object_or_404(Cart, user=request.user)
    
    if not cart.items.exists():
        messages.error(request, 'Your cart is empty!')
        return redirect('cart:cart_detail')
    
    if request.method == 'POST':
        # Create order
        order = Order.objects.create(
            user=request.user,
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            address=request.POST.get('address'),
            city=request.POST.get('city'),
            postal_code=request.POST.get('postal_code'),
            country=request.POST.get('country'),
            phone=request.POST.get('phone'),
            total_amount=cart.get_total_price()
        )
        
        # Create order items
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
            
            # Update product stock
            item.product.stock -= item.quantity
            item.product.save()
        
        # Clear the cart
        cart.items.all().delete()
        
        messages.success(request, f'Order #{order.id} placed successfully!')
        return redirect('orders:order_detail', order_id=order.id)
    
    context = {
        'cart': cart,
    }
    return render(request, 'orders/create_order.html', context)


@login_required
def order_detail(request, order_id):
    """Display order details"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    context = {
        'order': order,
    }
    return render(request, 'orders/order_detail.html', context)


@login_required
def order_list(request):
    """Display all orders for the logged-in user"""
    orders = Order.objects.filter(user=request.user)
    
    context = {
        'orders': orders,
    }
    return render(request, 'orders/order_list.html', context)
