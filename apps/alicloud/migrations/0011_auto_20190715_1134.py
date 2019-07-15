# Generated by Django 2.1.7 on 2019-07-15 03:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('alicloud', '0010_auto_20190712_1836'),
    ]

    operations = [
        migrations.RunSQL("DROP VIEW IF EXISTS alicloud_assets;"),
        migrations.RunSQL(
            "create view alicloud_assets as (select asset.id, type,instance_id,instance_name,status,node_id from alicloud_ecs as asset left join alicloud_ecs_nodes as node on asset.id = node.ecs_id) union all (select asset.id, type,instance_id,instance_name,status,node_id from alicloud_slb as asset left join alicloud_slb_nodes as node on asset.id = node.slb_id) union all (select asset.id, type,instance_id,instance_name,status,node_id from alicloud_rds as asset left join alicloud_rds_nodes as node on asset.id = node.rds_id) union all (select asset.id, type,instance_id,instance_name,status,node_id from alicloud_kvstore as asset left join alicloud_kvstore_nodes as node on asset.id = node.kvstore_id) union all (select asset.id, type,instance_id,instance_name,status,node_id from alicloud_oss as asset left join alicloud_oss_nodes as node on asset.id = node.oss_id);")
    ]
