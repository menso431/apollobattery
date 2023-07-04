import scrapy
import regex
import mysql.connector
import sys, os
from scrapy.spiders import Spider
from scrapy_crawlera import CrawleraMiddleware


class SpiderApolloSpider(scrapy.Spider):
    name = "spider_apollo"
    global db_connection
    global car_lastid
    db_connection = None
    allowed_domains = ["redbook.com.au/cars/results/"]
    start_urls = ["https://www.redbook.com.au/cars/results/"]

    user_agents = [
                    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
                    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
                    "Opera/9.80 (Windows NT 6.1; U; cs) Presto/2.2.15 Version/10.00"   
    ]
    db_connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="",
        database="apollo_scrap"
    )

    handle_httpstatus_list = [404]


    def parse(self, response):
        content = response.css("h3 > a::attr(href)").extract()
        for title in content:
            url = title
            detail_url = response.urljoin(url)
            print(url)
            # yield scrapy.Request(url=detail_url, callback=self.car_parse_detail, dont_filter=True)
