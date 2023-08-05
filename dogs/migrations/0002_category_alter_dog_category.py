# Generated by Django 4.2.4 on 2023-08-05 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Порода')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'порода',
                'verbose_name_plural': 'породы',
            },
        ),
        migrations.AlterField(
            model_name='dog',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogs.category', verbose_name='Порода'),
        ),
    ]