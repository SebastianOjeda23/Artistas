# Generated by Django 3.2 on 2024-10-25 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_artista', models.CharField(max_length=50)),
                ('nacionalidad', models.CharField(max_length=100)),
                ('fechanacimiento', models.DateField()),
                ('cancionescreada', models.IntegerField()),
                ('aniosactivo', models.IntegerField()),
            ],
        ),
    ]
