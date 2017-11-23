# -*- coding: utf-8 -*-
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    # start_urls = ['http://blog.jobbole.com/']
    start_urls = ['http://blog.jobbole.com/113089/']

    def parse(self, response):
        re_selector = response.xpath('/html/body/div[3]/div[3]/div[1]/div[1]/h1')       # Firefox取得的Xpath
        re_selector2 = response.xpath('//*[@id="post-113089"]/div[1]/h1')       # Chrome取得的Xpath
        re_selector3 = response.xpath('//*[@id="post-113089"]/div[1]/h1/text()')
        re_selector4 = response.xpath('//div[@class="entry-header"]/h1/text()')     # 自己筛选的xpath
        pass
