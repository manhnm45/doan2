from django.db import models
from home.models import demoscale
# Create your models here.
class weith(models.Model):
    weight_id = models.AutoField(primary_key=True)
    scale_id = models.ForeignKey(demoscale, default = None, on_delete = models.CASCADE)
    unit_weight = models.IntegerField(null = True)
    weight_current = models.IntegerField(null = True)
    number = models.IntegerField(null = True)

    def __str__(self):
        return f"{self.weight_id}, {self.scale_id}, {self.unit_weight}, {self.weight_current}, {self.number}"