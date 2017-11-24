命令行执行scrapy shell可以避免多次发送请求。
    scrapy shell http://blog.jobbole.com/113089/
    title = response.xpath('//div[@class="entry-header"]/h1/text()')
    title.extract()     # 取值
    title.extract()[0]  # extract()后是一个数组。
    title = response.xpath('//div[@class="entry-header"]/h1/text()').extract()[0]


scrapy shell proxy settings
    set http_proxy=http://proxy_addr:port
