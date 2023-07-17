from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Purchase, Vendor
from localight_egift.users.models import User

@login_required
def make_purchase(request):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=request.user.pk)
        vendor = get_object_or_404(Vendor, qr_code=request.POST.get('qr_code'))
        amount = request.POST.get('amount')
        gift_basket_id = request.POST.get('gift_basket_id')
        purchase = Purchase.objects.create(user=user, vendor=vendor, amount=amount, gift_basket_id=gift_basket_id)
        user.balance -= amount
        user.points += amount // 10
        user.save()
        return render(request, 'purchase_success.html', {'purchase': purchase})
    else:
        return render(request, 'make_purchase.html')

@login_required
def purchase_gift_basket(request):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=request.user.pk)
        if user.balance < 20:
            return render(request, 'purchase_gift_basket.html', {'error': 'Insufficient balance.'})
        purchase = Purchase.objects.create(user=user, amount=20, gift_basket_id=1)
        user.balance -= 20
        user.points += 20 // 10
        user.save()
        return render(request, 'purchase_success.html', {'purchase': purchase})
    else:
        return render(request, 'purchase_gift_basket.html')
