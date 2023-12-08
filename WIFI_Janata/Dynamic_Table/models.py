from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class JWData(models.Model):
    Date=models.DateField()
    TradeCode=models.CharField(max_length=50)
    High=models.DecimalField(max_digits=20, decimal_places=2)
    Low=models.DecimalField(max_digits=20, decimal_places=2)
    Open=models.DecimalField(max_digits=20, decimal_places=2)
    Close=models.DecimalField(max_digits=20, decimal_places=2)
    Volume=models.IntegerField()