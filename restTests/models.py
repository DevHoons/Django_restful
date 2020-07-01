from django.db import models


class Address(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created"]
