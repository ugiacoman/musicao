#Host: freesummarizer.com
#User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:35.0) Gecko/20100101 Firefox/35.0
#Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
#Accept-Language: en-US,en;q=0.5
#Accept-Encoding: gzip, deflate
#Referer: http://freesummarizer.com/
#Cookie: _jsuid=777245265; _ga=GA1.2.164138903.1423973625; __smToken=elPdHJINsP5LvAYhia6OAA68; __smListBuilderShown=true; _first_pageview=1; _gat=1; _eventqueue=%7B%22heatmap%22%3A%5B%7B%22type%22%3A%22heatmap%22%2C%22href%22%3A%22%252F%22%2C%22x%22%3A324%2C%22y%22%3A1800%2C%22w%22%3A640%7D%5D%2C%22events%22%3A%5B%5D%7D; PHPSESSID=28b0843d49700e134530fbe32ea62923; __smSmartbarShown=true
#Connection: keep-alive
#Content-Type: application/x-www-form-urlencoded
#Content-Length: 6044

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):

    s = MLStripper()
    s.feed(html)
    lyrics = s.get_data()
    return lyrics




# lyrics url and parses it
url = "http://www.azlyrics.com/lyrics/kendricklamar/therecipe.html"
r = requests.get(url)
soup = BeautifulSoup(r.content)
divs = soup.find_all("div")
div_list = []
for div in divs:
    div_list.append(div)
lyrics = div_list[6]    
strip_tags(str(lyrics))


text = str(lyrics)

browser = webdriver.Firefox()
browser.set_window_size(1280, 1024) # set browser size.
browser.get('http://www.freesummarizer.com') # Load page
browser.save_screenshot('screen.png')



username = browser.find_element_by_name('text')


browser.find_element_by_id("summarizebutton").click()
# browser.scroll(0,500)

username.clear()
username.send_keys(text)

password = browser.find_element_by_name('maxsentences')
password.clear()
password.send_keys('1')

password = browser.find_element_by_name('email')
password.clear()
password.send_keys('ulises.giacoman@gmail.com')

browser.find_element_by_name("submit").click()
browser.close()
