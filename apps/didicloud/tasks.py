# ~*~ coding: utf-8 ~*~
import json
import re
from celery import shared_task
from django.db import transaction
from django.db.models import Q
from ops.celery.decorator import register_as_period_task
from .models import *
from assets.models import Node
from assets.models import Asset as JAssets
from .utils import DiDiCloudUtil
from common.utils import get_logger, get_object_or_none
from django.conf import settings

logger = get_logger(__file__)


@shared_task
@register_as_period_task(interval=3600 * 24)
def sync_dc2_list_info_manual():
    logger.info('ready to sync didi cloud dc2 list')
    didi_util = DiDiCloudUtil()
    created, updated, failed = [], [], []
    j_created, j_updated, j_failed = [], [], []
    node = Node.root()
    Dc2.objects.all().update(status='Destory')
    for info in didi_util.get_dc2_instances():
        logger.info(json.dumps(info))
        dc2 = get_object_or_none(Dc2, instance_id=info.get('instance_id'))
        if not dc2:
            try:
                with transaction.atomic():
                    dc2 = Dc2.objects.create(**info)
                    node = auto_allocate_asset_node(info.get('instance_name'), 'dc2')
                    # need to add auto join node
                    dc2.nodes.set([node])
                    created.append(info['instance_name'])
            except Exception as e:
                failed.append('%s: %s' % (info['instance_name'], str(e)))
        else:
            for k, v in info.items():
                if v != '':
                    setattr(dc2, k, v)
            try:
                if not dc2.nodes.exclude(key='1').first():
                    logger.info('update node for root node dc2')
                    node = auto_allocate_asset_node(info.get('instance_name'), 'dc2')
                    dc2.nodes.set([node])
                dc2.save()
                updated.append(info['instance_name'])
            except Exception as e:
                failed.append('%s: %s' % (info['instance_name'], str(e)))

        if settings.AUTO_UPDATE_JUMPSERVER_ASSETS:
            asset = get_object_or_none(JAssets, number=info.get('instance_id'))
            if not asset:
                try:
                    with transaction.atomic():
                        hostname = info.get('instance_name')
                        admin_user, domain = auto_get_admin_and_domain(hostname)
                        attr = {
                            'number': info.get('instance_id'),
                            'ip': info.get('inner_ip'),
                            'port': 3299,
                            'protocol': 'ssh',
                            'protocols': 'ssh/3299',
                            'hostname': hostname,
                            'platform': 'Linux',
                            'domain': domain,
                            'admin_user': admin_user
                        }
                        asset = JAssets.objects.create(**attr)
                        # need to add auto join node
                        asset.nodes.set([node])
                        j_created.append(info['instance_name'])
                except Exception as e:
                    j_failed.append('%s: %s' % (info['instance_name'], str(e)))
            else:
                setattr(asset, 'hostname', info.get('instance_name'))
                setattr(asset, 'ip', info.get('inner_ip'))
                try:
                    asset.save()
                    j_updated.append(info['instance_name'])
                except Exception as e:
                    j_failed.append('%s: %s' % (info['instance_name'], str(e)))

    data = {
        'created': created,
        'created_info': 'Created {}'.format(len(created)),
        'updated': updated,
        'updated_info': 'Updated {}'.format(len(updated)),
        'failed': failed,
        'failed_info': 'Failed {}'.format(len(failed)),
        'valid': True,
        'msg': 'Created: {}. Updated: {}, Error: {}'.format(
            len(created), len(updated), len(failed))
    }
    logger.info('dc2 sync finish')
    logger.info(json.dumps(data))

    if settings.AUTO_UPDATE_JUMPSERVER_ASSETS:
        clean_destory_assets_in_jumpserver()
        j_data = {
            'created': j_created,
            'created_info': 'Created {}'.format(len(j_created)),
            'updated': j_updated,
            'updated_info': 'Updated {}'.format(len(j_updated)),
            'failed': j_failed,
            'failed_info': 'Failed {}'.format(len(j_failed)),
            'valid': True,
            'msg': 'Created: {}. Updated: {}, Error: {}'.format(
                len(j_created), len(j_updated), len(j_failed))
        }
        logger.info('jump server asset update finish')
        logger.info(json.dumps(j_data))
    return data


def clean_destory_assets_in_jumpserver():
    destroy_assets = Dc2.objects.values("instance_id").filter(status='Destory')
    JAssets.objects.filter(number__in=[asset.get('instance_id') for asset in destroy_assets]).delete()


def auto_get_admin_and_domain(name):
    admin_user, domain = None, None
    logger.info('try to auto get amdin_user and domain with {}'.format(name))
    num_list = re.findall(r"\d+", name)
    if len(num_list):
        name = name[:name.index(num_list[-1])]
    logger.info('try to find name {}'.format(name))
    asset = JAssets.objects.filter(hostname__contains=name).exclude(
        Q(admin_user=None) | Q(domain=None)).first()
    if asset:
        admin_user = asset.admin_user
        domain = asset.doamin
        logger.info('auto set {} admin_user:{} domain:{}'.format(name, admin_user, domain))
    return admin_user, domain


def auto_allocate_asset_node(name, asset_type):
    logger.info('auto allocate {} {}'.format(name, asset_type))
    num_list = re.findall(r"\d+", name)
    if len(num_list):
        name = name[:name.index(num_list[-1])]
    logger.info('auto allocate find name {}'.format(name))
    asset = None
    if asset_type == 'dc2':
        asset = Dc2.objects.filter(instance_name__contains=name).exclude(Q(nodes=None) | Q(nodes__key='1')).first()
    else:
        pass
    if asset:
        node = asset.nodes.exclude(key='1').first()
        if node:
            logger.info('auto allocate {} to {}'.format(name, node.value))
            return node
        else:
            logger.info('auto allocate {} to root node'.format(name))
            return Node.root()
    else:
        logger.info('auto allocate {} to root node'.format(name))
        return Node.root()
