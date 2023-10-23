from scrapy.crawler import CrawlerProcess
from scrapy_project.scrapy_project.spiders.quotes_spider import QuotesSpider, AuthorsSpider

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(QuotesSpider)
    process.crawl(AuthorsSpider)
    process.start()