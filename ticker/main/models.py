from django.db import models

class Price(models.Model):
    foster = models.DecimalField(max_digits=5, decimal_places=2)
    g_t = models.DecimalField(max_digits=5, decimal_places=2)
    captain_morgan = models.DecimalField(max_digits=5, decimal_places=2)
    pampero = models.DecimalField(max_digits=5, decimal_places=2)
    roe_and_co = models.DecimalField(max_digits=5, decimal_places=2)
    zaconey = models.DecimalField(max_digits=5, decimal_places=2)
    vodka_redbull = models.DecimalField(max_digits=5, decimal_places=2)
    interval_index = models.DecimalField(max_digits=5, decimal_places=2)

    
