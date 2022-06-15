from django.core.validators import MaxValueValidator
from django.db import models


class Type_of_training(models.Model):
    type_training = models.CharField(max_length=255)
    kkal_in_hour = models.IntegerField(validators=[MaxValueValidator(2500)])

    def __str__(self):
        return self.type_training

    class Meta:
        verbose_name = 'Виды тренировок'
        verbose_name_plural = 'Виды тренировок'
        ordering = ['type_training']


class Training_trecker(models.Model):
    id_users = models.ForeignKey('calculator.Profile', on_delete=models.CASCADE)
    id_training = models.ForeignKey(Type_of_training, on_delete=models.PROTECT)
    day_create = models.DateField(auto_now_add=True)
    duration_training_min = models.IntegerField(validators=[MaxValueValidator(1440)])
    burned_kkal = models.FloatField(null=True)

    def __str__(self):
        return str(self.burned_kkal)

    class Meta:
        verbose_name = 'Трекер тренировок'
        verbose_name_plural = 'Трекер тренировок'
        ordering = ['day_create', 'id']
