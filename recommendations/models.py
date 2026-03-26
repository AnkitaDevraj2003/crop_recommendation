from django.db import models

class recommendation(models.Model):
    soil_type = models.CharField(
        max_length=100,
    choices=[
        ('alluvial', 'Alluvial'),
        ('black', 'Black'),
        ('red', 'Red'),
        ('laterite', 'Laterite'),
        ('sandy', 'Sandy'),
        ('clay', 'Clay'),
        ('loamy', 'Loamy')
    ]
    )
    water_source = models.CharField(max_length=100)
    water_availability = models.CharField(
        max_length=50,
    choices=[
        ('continuous', 'Continuous'),
        ('seasonal', 'Seasonal'),
        ('scarce', 'Scarce')
    ]
    )
    crop_duration = models.IntegerField()
    location = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
