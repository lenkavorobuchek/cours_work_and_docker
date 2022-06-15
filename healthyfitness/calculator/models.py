from django import forms
from audioop import reverse
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


User._meta.get_field('email')._unique = True

class Calculator(models.Model):
    age = models.CharField('', max_length=3)
    weight = models.CharField('', max_length=5)
    growth = models.CharField('', max_length=3)
    select_gender = (
        (None, 'Укажите пол'),
        ('1', "Мужской"),
        ('2', "Женский")
    )
    gender = models.CharField(max_length=1, choices=select_gender, default=None)
    select_aim = (
        (None, 'Укажите цель'),
        ('1', "Похудение"),
        ('2', "Поддержание веса"),
        ('3', "Набор мышечной массы"),
    )
    user_aim = models.CharField(max_length=1, choices=select_aim)
    select_activity = (
        (None, 'Укажите активность'),
        ('1', "Отсутствие активности"),
        ('2', "Низкая активность"),
        ('3', "Средняя активность"),
        ('4', "Высокая активность"),
        ('5', "Экстремальная активность"),
    )
    user_activity = models.CharField(max_length=100, choices=select_activity)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    age = models.IntegerField(null=True)
    weight = models.FloatField(null=True)
    gender = models.CharField(max_length=8, null=True)
    growth = models.IntegerField(null=True)
    Activity_level = models.CharField(max_length=100, null=True)
    user_aim = models.CharField(max_length=30, null=True)
    needed_kkal = models.IntegerField(null=True)
    needed_proteins = models.IntegerField(null=True)
    needed_fats = models.IntegerField(null=True)
    needed_carbohydrates = models.IntegerField(null=True)
    photo = models.ImageField(upload_to="photos_profile/%Y/%m/%d", null=True, blank=True, default="iconForPersonalarea.png")

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def update_profile_signal(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    @receiver(pre_save, sender='weight.Weight_trecker')
    def update_profile_weight(sender, instance, **kwargs):
        if Profile.objects.get(user=instance.id_users).weight != instance.weight:
            Profile.objects.filter(user=instance.id_users).update(weight=instance.weight)
