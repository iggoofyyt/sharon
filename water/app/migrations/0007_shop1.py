# Generated by Django 5.0.1 on 2024-02-04 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_employee_price_action'),
    ]

    operations = [
        migrations.CreateModel(
            name='shop1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p1', models.CharField(max_length=9)),
                ('p2', models.CharField(max_length=9)),
                ('p3', models.CharField(max_length=9)),
                ('p4', models.CharField(max_length=9)),
                ('nme', models.CharField(max_length=30)),
            ],
        ),
    ]
