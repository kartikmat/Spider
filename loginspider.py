# Test Login Spider
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request


login_url = "https://login.libproxy1.usc.edu/login?url=https://global.factiva.com/ha/default.aspx"
user_name = b"kmathur"
pswd = b""
response_page = "https://global-factiva-com.libproxy1.usc.edu/"


class MySpider(scrapy.Spider):
    name = 'lspider'

    def start_requests(self):
        return [scrapy.FormRequest(login_url,
                               formdata={'user': user_name, 'pass': pswd},
                               callback=self.logged_in)]

    def logged_in(self, response):
        # login failed
        if b"authentication failed" in response.body:
            print ("Login failed")
        # login succeeded
        else:
            print ('login succeeded')
            # return Request(url=response_page,
            #        callback=self.parse_responsepage)

    def parse_responsepage(self, response):
        hxs = HtmlXPathSelector(response)
        yum = hxs.select('//span/@enHeadline')

    def parse_page(self, response):
    
    	hxs = HtmlXPathSelector(response)
    	images = hxs.select('//img')
    # .. do something with them
    	links = hxs.select('//a/@href')

    # Yield a new request for each link we found
   	for link in links:
        	yield Request(url=link, callback=self.parse_page)

def main():
    test_spider = MySpider(scrapy.Spider)
    test_spider.start_requests()

if __name__ == "__main__":
    main()
