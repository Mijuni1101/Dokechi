from django.db import models

class Consumable(models.Model):
    name = models.CharField(max_length=100)
    total_quantity = models.PositiveIntegerField(default=0)
    threshold = models.PositiveIntegerField(default=1)  # 残量警告のしきい値

    def __str__(self):
        return self.name

class UsageLog(models.Model):
    consumable = models.ForeignKey(Consumable, on_delete=models.CASCADE)
    date = models.DateField()
    quantity_used = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.consumable.name} on {self.date}"
from django.db import models

# Create your models here.
