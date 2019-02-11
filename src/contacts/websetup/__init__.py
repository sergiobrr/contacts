# -*- coding: utf-8 -*-
"""Setup the contacts application"""

import logging

from contacts.config.environment import load_environment

__all__ = ['setup_app']

log = logging.getLogger(__name__)

from .schema import setup_schema
from .bootstrap import bootstrap


def setup_app(command, conf, vars):
    """Place any commands to setup contacts here"""
    load_environment(conf.global_conf, conf.local_conf)
    setup_schema(command, conf, vars)
    bootstrap(command, conf, vars)
