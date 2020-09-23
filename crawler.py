import time
import json
from selenium import webdriver

class SEcrawler():
    def tutorial(self):
        links = {
            "selenium sheet": "https://stackoverflow.com/questions/26393231/using-python-requests-with-javascript-pages",
            "scrapt js chart from selenium": "https://stackoverflow.com/questions/39864796/how-to-scrape-charts-from-a-website-with-python",
            "selenium from medium": "https://medium.com/@ivantay2003/selenium-cheat-sheet-in-python-87221ee06c83",
            "selenium crawl js chart": "https://www.cnblogs.com/sanduzxcvbnm/p/10276617.html"
        }
        for link, url in enumerate(links):
            print(link, url)

    def crawler(self, currency):

        website = 'https://www.esunbank.com.tw/bank/personal/deposit/rate/forex/exchange-rate-chart?Currency=' + currency + '/TWD'
        driver = webdriver.Chrome()
        driver.get(website)
        time.sleep(2)

        driver.find_element_by_xpath('//input[@type="radio" and @name="radio"]')
        time.sleep(2)

        driver.execute_script("document.getElementsByClassName('midBtn btns')[0].click()")

        page = 0
        data = {}
        while page < 20:
            element = driver.find_element_by_class_name('inteTable')
            tr_content = element.find_elements_by_tag_name("tr")
            for tr in tr_content:
                text = tr.get_attribute("innerHTML")
                try:
                    text = text.replace('<td class="itemTtitle">', '')\
                        .replace('</td><td class="lastTd">',', ')\
                        .replace("</td><td>",', ')\
                        .replace('</td>','').split(', ')
                    date = text[0]
                    buy = text[1]
                    sell = text[2]
                    if date:
                        data[date] = {'buy': buy, 'sell': sell}
                except:
                    pass # not date type data
            driver.execute_script("document.getElementsByClassName('down active')[0].click()") # next page
            page += 1
        return json.dumps({currency: data}, indent=4)


# if __name__ == "__main__":
#     currencys = ['USD']#, 'CNY', 'AUD', 'EUR', 'HKD']
#
#     sec = SEcrawler()
#
#     for currency in currencys:
#         result = sec.crawler(currency)
#         print(result)