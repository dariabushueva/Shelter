# Generated by Django 4.2.4 on 2023-08-26 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0003_alter_dog_birth_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Кличка')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='dogs/', verbose_name='Фото')),
                ('birth_day', models.DateField(blank=True, null=True, verbose_name='Дата Рождения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogs.category', verbose_name='Порода')),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogs.dog', verbose_name='Собака')),
            ],
            options={
                'verbose_name': 'предок',
                'verbose_name_plural': 'предки',
            },
        ),
    ]
