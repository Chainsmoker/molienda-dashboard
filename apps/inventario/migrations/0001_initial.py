# Generated by Django 4.1.7 on 2023-03-12 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, unique=True)),
                ('stock', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('observacion', models.TextField()),
            ],
        ),
    ]
