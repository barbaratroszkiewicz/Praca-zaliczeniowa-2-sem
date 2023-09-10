from django.db import models

# Create your models here.

class Pizza(models.Model):
    class PizzaType(models.TextChoices):
        UNKNOWN = 'Unknown'
        MARGHERITA = 'Margherita'
        PEPPERONI = 'Pepperoni'
        HAWAIIAN = 'Hawaiian'
        SUPREME = 'Supreme'
    name = models.CharField(blank=False, default='Unknown',
                            max_length=150, unique=True)
    year_of_birth = models.IntegerField(blank=True, null=True)
    year_of_death = models.IntegerField(blank=True, null=True)
    pizza_type = models.CharField(blank=False,
                                  default=PizzaType.UNKNOWN,
                                  max_length=25,
                                  choices=PizzaType.choices)

    def __str__(self):
        return f'{self.id}: {self.name}'
