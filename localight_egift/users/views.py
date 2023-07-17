from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import User
from localight_egift.vendors.models import Vendor
import stripe

stripe.api_key = "sk_test_51NUfRnER8Gw2gWMvtgdUZVFTucNKne9Me7OdoCEpR7Ef92r0Q3M6rco9bTl8TGie7vZxBQOuGD6dQ0b4fZV54EbD00mqbXDrkS"

@login_required
def profile(request):
    user = User.objects.get(pk=request.user.pk)
    return render(request, 'profile.html', {'user': user})

@login_required
def load_money(request):
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.pk)
        amount = int(request.POST.get('amount'))
        if amount < 10:
            return render(request, 'load_money.html', {'error': 'Minimum load amount is $10.'})
        stripe.Charge.create(
            amount=amount * 100,  # Stripe expects the amount in cents
            currency='usd',
            description=f'Load money for {user.username}',
            source=request.POST.get('stripeToken')
        )
        user.balance += amount
        user.save()
        return redirect('users:profile')
    else:
        return render(request, 'load_money.html')

@login_required
def scan_qr_code(request):
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.pk)
        qr_code = request.POST.get('qr_code')
        vendor = Vendor.objects.get(qr_code=qr_code)
        amount = vendor.qr_code.split('=')[-1]
        user.balance += int(amount)
        user.save()
        return redirect('users:profile')
    else:
        return render(request, 'scan_qr_code.html')
