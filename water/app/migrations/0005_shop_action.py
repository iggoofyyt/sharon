# Generated by Django 4.2 on 2024-01-30 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_price_shop'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='action',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
