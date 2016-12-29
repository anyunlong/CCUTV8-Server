# -*- coding: utf-8 -*-

# Scrapy settings for crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'crawler'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'

ROBOTSTXT_OBEY = True

import sys
sys.path.append('/Users/Oneself/Desktop/ccutv8/server')

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'server.settings'

# ITEM_PIPELINES = {
#     'crawler.pipelines.MysqlPipeline': 300,
# }