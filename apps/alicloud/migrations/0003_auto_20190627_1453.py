# Generated by Django 2.1.7 on 2019-06-27 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alicloud', '0002_auto_20190627_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ecs',
            name='public_ip',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='PublicIp'),
        ),
    ]
