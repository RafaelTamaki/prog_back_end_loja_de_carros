# Generated by Django 4.2.6 on 2023-11-07 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja_de_carros', '0002_carro_montadora'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
    ]
