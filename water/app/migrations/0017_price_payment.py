# Generated by Django 5.0.2 on 2024-02-15 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_detail_emp'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='payment',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
