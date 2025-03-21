import scrapy

class TorrentSpider(scrapy.Spider):
    name = "torrents"
    start_urls = ["https://www.1337x.to/popular-movies"]
    
    def parse(self, response):
        for row in response.css("table.table-list tbody tr"):
            yield {
                "title": row.css("td.name a:nth-of-type(2)::text").get(),
                "link": response.urljoin(row.css("td.name a:nth-of-type(2)::attr(href)").get())
            }
