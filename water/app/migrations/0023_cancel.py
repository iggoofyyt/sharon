# Generated by Django 5.0.1 on 2024-02-20 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_detail_q1_detail_q2_detail_q3_detail_q4'),
    ]

    operations = [
        migrations.CreateModel(
            name='cancel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('amount', models.IntegerField()),
                ('action', models.CharField(max_length=30)),
            ],
        ),
    ]
