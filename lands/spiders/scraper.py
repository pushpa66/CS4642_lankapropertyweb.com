import scrapy


class RecipesSpider(scrapy.Spider):
    name = "lands"
    start_urls = [
        'https://www.lankapropertyweb.com/land/index.php',
    ]

    def parse(self, response):
        for inner_article in response.css('h4.listing-titles'):
            yield response.follow(inner_article.css('a::attr(href)').extract_first(), callback=self.parse_page)
        next_page = response.css('div ul.pagination li.pagination_arrows a::attr(href)').extract()[1]
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)

    def parse_page(self, response):

        yield {
            'title': response.xpath('//*[@class="details-heading.details-property"]/h1/text()').extract(),
            # 'location': response.xpath('//*div[@class="col-md-9.col-sm-10.col-xs-12"]/span[@class="details-location"]/text()').extract_first(),
            # 'price': response.css('div.price-detail').extract_first()
        }