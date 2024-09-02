# Generated by Django 5.0.6 on 2024-07-07 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('imagen', models.ImageField(upload_to='imagenes/')),
                ('nombre', models.CharField(max_length=100)),
                ('tamaño', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
