#! /usr/bin/env python3
#-*- coding:utf-8 -*-


#把config_default.py作为开发环境的标准配置

__author__='liuxver'

configs={
	'db':{
	'host':'127.0.0.1',
	'port':3306,
	'user':'www-data',
	'password':'www-data',
	'database':'awesome'#数据库名称
	},
	'session':{
	'secret':'AwEsOmE'
	}
}