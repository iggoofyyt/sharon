# Generated by Django 5.0.2 on 2024-02-10 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_detail_action'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='deliver',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
