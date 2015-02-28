# Host: freesummarizer.com
# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:35.0) Gecko/20100101 Firefox/35.0
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
# Accept-Language: en-US,en;q=0.5
# Accept-Encoding: gzip, deflate
# Referer: http://freesummarizer.com/
# Cookie: _jsuid=777245265; _ga=GA1.2.164138903.1423973625; __smToken=elPdHJINsP5LvAYhia6OAA68; __smListBuilderShown=true; _first_pageview=1; _gat=1; _eventqueue=%7B%22heatmap%22%3A%5B%7B%22type%22%3A%22heatmap%22%2C%22href%22%3A%22%252F%22%2C%22x%22%3A324%2C%22y%22%3A1800%2C%22w%22%3A640%7D%5D%2C%22events%22%3A%5B%5D%7D; PHPSESSID=28b0843d49700e134530fbe32ea62923; __smSmartbarShown=true
# Connection: keep-alive
# Content-Type: application/x-www-form-urlencoded
# Content-Length: 6044
import string
import mechanize
import requests
from bs4 import BeautifulSoup
import re
# lyrics url and parses it

# rest = str(input('Please input song: '))
# br = mechanize.Browser()
# br.addheaders = [('User-agent', 'Mozilla/5.0')]
# br.set_handle_robots(False)

string = str(raw_input('Please input a song: '))
parsed = ''
for char in string:
	if char == ' ':
		char = '+'
	parsed = parsed + char

url = 'http://www.google.com/search?q=' + 'site:azlyrics.com+' + parsed

r = requests.get(url)
soup = BeautifulSoup(r.content)

href_list = []
i = 0
for a in soup.find_all('a', href=True):
	href_list.append(a)
blurURL = str(href_list[24])
blurURL = blurURL[16:]
sep = 'html'

hello = blurURL.split(sep)[0]
url = hello + 'html'


# url = "http://www.azlyrics.com/lyrics/kendricklamar/therecipe.html"
# r = requests.get(url)
# soup = BeautifulSoup(r.content)
# divs = soup.find_all("div")
# div_list = []
# for div in divs:
#     div_list.append(div)
# lyrics = div_list[6]    

# text = str(lyrics)

# dcap = dict(DesiredCapabilities.FIREFOX)
# dcap["phantomsjs.page.settings.userAgent"] = (
#     "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36"

#     )

# driver = webdriver.Firefox()
# driver.set_window_size(1280, 1024) # set browser size.
# driver.get('http://www.freesummarizer.com') # Load page



# summarize_box = driver.find_element_by_xpath('//*[@id="summarizebutton"]/i')
# summarize_box.click()
# #driver.save_screenshot('screen.png')


# text_box = driver.find_element_by_xpath('//*[@id="text"]')
# delete = (Keys.CONTROL, "a")
# text_box.send_keys(delete)
# text_box.send_keys(Keys.DELETE)
# text_box.send_keys(text)

# m_sentences = driver.find_element_by_xpath('//*[@id="summarizecontainer"]/div/div/form/div/input[2]')
# m_sentences.send_keys(send_keys + '1')


# email = driver.find_element_by_xpath('//*[@id="summarizecontainer"]/div/div/form/div/input[3]')
# email.send_keys(send_keys + 'ulises.giacoman@gmail.com')

# submit = driver.find_element_by_xpath('//*[@id="summarizecontainer"]/div/div/form/div/div/input')
# submit.click()


# browser.find_element_by_id("summarizebutton").click()
# # browser.scroll(0,500)
# #username.clear()
# username.send_keys(text)

# password = browser.find_element_by_name('maxsentences')
# #password.clear()
# password.send_keys('1')

# password = browser.find_element_by_name('email')
# #password.clear()
# password.send_keys('ulises.giacoman@gmail.com')

# browser.find_element_by_name("submit").click()
# browser.close()