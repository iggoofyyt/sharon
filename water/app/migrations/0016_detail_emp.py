# Generated by Django 5.0.1 on 2024-02-11 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_price_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='emp',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
