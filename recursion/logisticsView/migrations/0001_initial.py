# Generated by Django 2.2.5 on 2020-03-13 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('product_name', models.CharField(max_length=100)),
                ('available_quantity', models.IntegerField()),
                ('rate', models.IntegerField()),
            ],
        ),
    ]