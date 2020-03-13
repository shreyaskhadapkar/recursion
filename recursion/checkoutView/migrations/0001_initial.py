# Generated by Django 2.2.5 on 2020-03-13 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userView', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userView.Cart')),
            ],
        ),
    ]
