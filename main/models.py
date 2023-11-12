from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    customer_name = models.CharField(max_length=200, blank=False, null=False)
    phone_number = models.IntegerField(blank=False, null=False)
    address = models.TextField(blank=False, null=False)
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
