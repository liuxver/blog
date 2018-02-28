#! /usr/bin/env python3
#-*- coding:utf-8 -*-

__author__='liuxver'

configs=configs_default.configs

try:
	import config_override
	configs=merge(configs,config_override.configs)
except ImportError:
	pass

