# Generated by Django 2.1.7 on 2019-06-27 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alicloud', '0004_ecs_nodes'),
    ]

    operations = [
        migrations.AddField(
            model_name='ecs',
            name='instance_type',
            field=models.CharField(default=1, max_length=128, verbose_name='InstanceType'),
            preserve_default=False,
        ),
    ]
