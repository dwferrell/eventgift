from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    qr_code = models.CharField(max_length=255)

    def __str__(self):
        return self.name
