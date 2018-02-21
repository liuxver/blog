#! /usr/bin/env python3
#-*- coding:utf-8 -*-

import logging;logging.basicConfig(level=logging.INFO)
import asyncio,os,json,time
from datetime import datetime
from aiohttp import web

def index(request):
	#headers={'content-type':'text/html' 这个可以按照格式显示
	#因为Google打开的是下载文件
	return web.Response(body=b'<h1>Awesome</h1>',headers={'content-type':'text/html'})

@asyncio.coroutine
def init(loop):
	app=web.Application(loop=loop)
	app.router.add_route('GET','/',index)
	srv=yield from loop.create_server(app.make_handler(),'127.0.0.1',9000)
	logging.info('Server start at http://127.0.0.1:9000...')
	return srv

loop=asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()


