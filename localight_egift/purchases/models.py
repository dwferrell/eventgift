from django.db import models
from localight_egift.users.models import User
from localight_egift.vendors.models import Vendor

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    gift_basket_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Purchase {self.id} by {self.user.username} for {self.amount}'
