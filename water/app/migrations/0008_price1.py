# Generated by Django 5.0.1 on 2024-02-04 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_shop1'),
    ]

    operations = [
        migrations.CreateModel(
            name='price1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n1', models.IntegerField()),
                ('n2', models.IntegerField()),
                ('n3', models.IntegerField()),
                ('n4', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('action', models.CharField(max_length=50)),
            ],
        ),
    ]
