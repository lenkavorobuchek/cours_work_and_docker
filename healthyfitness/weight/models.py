from datetime import date

from django.core.validators import MaxValueValidator
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, pre_delete

from calculator.models import Profile


class Weight_trecker(models.Model):
    id_users = models.ForeignKey('calculator.Profile', on_delete=models.CASCADE)
    day_create = models.DateField(auto_now_add=True)
    weight = models.FloatField(null=True, validators=[MaxValueValidator(400)])

    def __str__(self):
        return str(self.weight)

    @receiver(pre_save, sender=Profile)
    def update_profile_signal(sender, instance, **kwargs):
        # print(instance.weight)
        # print(Profile.objects.get(user=instance).weight)
        if instance.weight and Profile.objects.get(user=instance).weight != instance.weight:
            if Weight_trecker.objects.filter(id_users=instance, day_create=date.today()):
                Weight_trecker.objects.filter(id_users=instance).update(weight=instance.weight)
            else:
                Weight_trecker.objects.create(id_users=instance, weight=instance.weight)

    # @receiver(pre_delete, sender=Profile)
    # def del_weight_profile(sender, instance, **kwargs):
    #     if Weight_trecker.objects.filter(id_users=instance):
    #         Weight_trecker.objects.filter(id_users=instance).delite()

    class Meta:
        verbose_name = 'Трекер веса'
        verbose_name_plural = 'Трекер веса'
        ordering = ['day_create']
