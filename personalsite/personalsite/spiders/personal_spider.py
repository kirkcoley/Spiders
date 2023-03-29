import scrapy

class linkSpider(scrapy.Spider):
    name = "links"

    def start_requests(self):
        urls = [
            'https://www.kirkcoley.com'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for post in response.xpath("//h2[@class='wp-block-post-title']"):
            yield {
                'text' : post.xpath("descendant::text()").get(),
                'link' : post.xpath("descendant::a/@href").get()
            }
 