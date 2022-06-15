from django.core.validators import MaxValueValidator
from django.db import models


class Water_tracker(models.Model):
    id_users = models.ForeignKey('calculator.Profile', on_delete=models.CASCADE)
    day_create = models.DateField(auto_now_add=True)
    number_of_glasses = models.IntegerField(validators=[MaxValueValidator(50)])

    def __str__(self):
        return str(self.number_of_glasses)

    class Meta:
        verbose_name = 'Трекер воды'
        verbose_name_plural = 'Трекер воды'
        ordering = ['day_create']

