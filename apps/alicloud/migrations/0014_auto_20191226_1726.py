# Generated by Django 2.1.7 on 2019-12-26 09:26

import alicloud.models.template
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0034_auto_20190705_1348'),
        ('alicloud', '0013_asset'),
    ]

    operations = [
        migrations.CreateModel(
            name='EcsCreateRecord',
            fields=[
                ('org_id', models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('instance_name', models.CharField(max_length=256)),
                ('amount', models.IntegerField()),
                ('suffix_number', models.CharField(max_length=256)),
                ('auto_renew', models.BooleanField()),
                ('uid', models.CharField(max_length=256)),
                ('result_ids', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EcsTemplate',
            fields=[
                ('org_id', models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(default='', max_length=512)),
                ('region', models.CharField(max_length=256)),
                ('zone', models.CharField(max_length=256)),
                ('instance_type', models.CharField(max_length=256)),
                ('cores', models.IntegerField()),
                ('memory', models.IntegerField()),
                ('image', models.CharField(max_length=256)),
                ('sg', models.CharField(max_length=256)),
                ('network_type', models.CharField(choices=[('classic', 'classic'), ('vpc', 'vpc')], max_length=20)),
                ('vpc', models.CharField(blank=True, default=None, max_length=256, null=True)),
                ('vswitch', models.CharField(blank=True, default=None, max_length=256, null=True)),
                ('password', models.CharField(blank=True, default='', max_length=256, null=True)),
                ('password_inherit', models.BooleanField(default=True)),
                ('system_disk_category', models.CharField(choices=[('cloud', 'cloud'), ('cloud_efficiency', 'cloud_efficiency'), ('cloud_ssd', 'cloud_ssd'), ('cloud_essd', 'cloud_essd')], default='cloud_efficiency', max_length=256)),
                ('system_disk_size', models.IntegerField(default=40)),
                ('data_disk_info', models.TextField()),
                ('instance_name', models.CharField(max_length=256)),
                ('instance_charge_type', models.CharField(choices=[('PrePaid', 'PrePaid'), ('PostPaid', 'PostPaid')], default='PrePaid', max_length=64)),
                ('has_public_ip', models.BooleanField(default=False, null=True)),
                ('internet_bandwidth', models.IntegerField(default=0, null=True)),
                ('internet_charge_type', models.CharField(choices=[('PayByTraffic', 'PayByTraffic'), ('PayByBandwidth', 'PayByBandwidth')], default='PayByBandwidth', max_length=64)),
                ('period', models.IntegerField(default=1)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date created')),
                ('admin_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='assets.AdminUser', verbose_name='Admin user')),
                ('domain', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='assets.Domain', verbose_name='Domain')),
                ('nodes', models.ManyToManyField(default=alicloud.models.template.default_node, related_name='ecs_template', to='assets.Node', verbose_name='Nodes')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='ecscreaterecord',
            name='template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='alicloud.EcsTemplate', verbose_name='Template'),
        ),
    ]
