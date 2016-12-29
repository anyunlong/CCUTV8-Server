# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import django
django.setup()

import scrapy
from scrapy_djangoitem import DjangoItem
from v8.models import Cartoon, Episode
#
class CartoonItem(DjangoItem):
    django_model = Cartoon
    name = scrapy.Field()
    url = scrapy.Field()

class EpisodeItem(DjangoItem):
    django_model = Episode
    title = scrapy.Field()
    url = scrapy.Field()
    cartoon = scrapy.Field()