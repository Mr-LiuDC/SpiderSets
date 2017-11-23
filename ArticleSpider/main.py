# -*- coding: utf-8 -*-
import os
import sys

from scrapy.cmdline import execute

__author__ = "LEO"


# print(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "jobbole"]) # 在命令行执行scrapy crawl jobbole一样的效果
