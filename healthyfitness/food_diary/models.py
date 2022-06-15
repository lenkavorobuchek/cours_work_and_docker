from audioop import reverse

from django.core.validators import MaxValueValidator
from django.db import models
from calculator.models import Profile


class Type_of_food(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = 'Категории еды'
        verbose_name_plural = 'Категории еды'


class Food(models.Model):
    name_of_product = models.CharField(max_length=255)
    kkal = models.IntegerField(validators=[MaxValueValidator(2500)])
    proteins = models.FloatField(max_length=6)
    fats = models.FloatField(max_length=6)
    carbohydrates = models.FloatField(max_length=6)
    type_of_food = models.ForeignKey(Type_of_food, on_delete=models.PROTECT)

    def __str__(self):
        return self.name_of_product

    class Meta:
        verbose_name = 'Еда'
        verbose_name_plural = 'Еда'
        ordering = ['name_of_product']


class Diary_of_food(models.Model):
    id_users = models.ForeignKey('calculator.Profile', on_delete=models.CASCADE)
    id_food = models.ForeignKey(Food, on_delete=models.PROTECT)
    day_create = models.DateField(auto_now_add=True)
    grams = models.IntegerField(validators=[MaxValueValidator(3000)])
    consumed_kkal = models.FloatField(null=True)
    consumed_proteins = models.FloatField(null=True)
    consumed_fats = models.FloatField(null=True)
    consumed_carbohydrates = models.FloatField(null=True)

    def __str__(self):
        return str(self.id_food)

    class Meta:
        verbose_name = 'Дневник питания'
        verbose_name_plural = 'Дневник питания'
        ordering = ['day_create']
