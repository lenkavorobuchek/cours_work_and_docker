from django.db import migrations, models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion



class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_user',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('slag', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('age', models.IntegerField(max_length=3, null=True)),
                ('weight', models.FloatField(max_length=3, null=True)),
                ('gender', models.CharField(max_length=8, null=True)),
                ('growth', models.IntegerField(max_length=3, null=True)),
                ('Activity_level', models.CharField(max_length=100, null=True)),
                ('user_aim', models.CharField(max_length=30, null=True)),
                ('needed_kkal', models.FloatField(max_length=5, null=True)),
                ('needed_proteins', models.FloatField(max_length=5, null=True)),
                ('needed_fats', models.FloatField(max_length=5, null=True)),
                ('needed_carbohydrates', models.FloatField(max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Calculator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=3, verbose_name='')),
                ('weight', models.CharField(max_length=5, verbose_name='')),
                ('growth', models.CharField(max_length=3, verbose_name='')),
                ('gender', models.CharField(choices=[(None, 'Укажите пол'), ('1', 'Мужской'), ('2', 'Женский')], default=None, max_length=1)),
                ('user_aim', models.CharField(choices=[(None, 'Укажите цель'), ('1', 'Похудение'), ('2', 'Поддержание веса'), ('3', 'Набор мышечной массы')], max_length=1)),
                ('user_activity', models.CharField(choices=[(None, 'Укажите активность'), ('1', 'Отсутствие активности'), ('2', 'Низкая активность'), ('3', 'Средняя активность'), ('4', 'Высокая активность'), ('5', 'Экстремальная активность')], max_length=100)),
            ],
        ),
    ]
