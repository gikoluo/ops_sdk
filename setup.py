#!/usr/bin/env python
# -*-coding:utf-8-*-
""""
author : shenshuo
date   : 2018年2月5日13:37:54
desc   : OPS SDK
"""
from distutils.core import setup

__version__ = '0.0.21'

setup(
    name='opssdk',
    version=__version__,
    packages=['opssdk', 'opssdk.logs', 'opssdk.operate', 'opssdk.install', 'opssdk.get_info', 'opssdk.utils', 'websdk'
              ,'websdk.apis'],
    url='https://github.com/ss1917/ops_sdk/',
    license='',
    install_requires=['fire==0.1.3', 'shortuuid', 'pymysql==0.9.3', 'sqlalchemy==1.3.13', 'pika==1.1.0', 'PyJWT',
                      'Crypto==1.4.1', 'requests', 'redis==2.10.6', 'tornado>=5.0',
                      'aliyun-python-sdk-core-v3==2.13.11', 'aliyun-python-sdk-dysmsapi', 'python-dateutil==2.7.5',
                      'ldap3==2.6', 'pycryptodome'],
    author='shenshuo',
    author_email='191715030@qq.com',
    description='SDK of the operation and maintenance script'
                'logs'
                'operate'
)
