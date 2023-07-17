from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Purchase
from localight_egift.users.models import User

@login_required
def make_purchase(request):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=request.user.pk)
        amount = request.POST.get('amount')
        purchase = Purchase.objects.create(user=user, amount=amount)
        user.balance -= amount
        user.points += amount // 10
        user.save()
        return render(request, 'purchase_success.html', {'purchase': purchase})
    else:
        return render(request, 'make_purchase.html')
