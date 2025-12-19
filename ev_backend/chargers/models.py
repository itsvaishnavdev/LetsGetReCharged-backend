from django.db import models

class EVCharger(models.Model):
    CHARGER_TYPES = (
        ('AC', 'AC'),
        ('DC', 'DC'),
        ('FAST', 'FAST'),
    )

    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    charger_type = models.CharField(max_length=10, choices=CHARGER_TYPES)
    power_kw = models.IntegerField(default=0)

    is_available = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
