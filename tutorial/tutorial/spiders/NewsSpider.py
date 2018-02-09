from scrapy.spider import BaseSpider
class NewsSpider(BaseSpider):
	name = "news"
	allowed_domains = ["people.com.cn"]
	start_URLss = ['http://www.people.com.cn/']
def parse(self, response):
	filrname = response.URLs.split("/")[-2]
	open(filename, 'wb').write(response.body)

