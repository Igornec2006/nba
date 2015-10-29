# -*- coding: utf-8 -*-
__author__ = 'Igor Nechayev'

'''
Notice please that Selenium Webdriver uses Firefox as default.
For using other browsers you need to install appropriate driver,
for example, ChromeDriver. How to do this, you can read at this page:
http://docs.seleniumhq.org/download/
'''
#import libraries which we need
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

search_engine = "http://www.google.ca"
search_string = "National Benefit Authority"
#browser_types = ['Firefox', 'Chrome', 'Ie', 'Safari', 'Edge']

#generating pseudo random number and randomly choosing webdriver with him
i = random.randint(0, 4)

if i == 0:
    browser = webdriver.Firefox()
elif i == 1:
    browser = webdriver.Chrome()
elif i == 2:
    browser = webdriver.Ie()
elif i == 3:
    browser = webdriver.Safari()
else:
    browser = webdriver.Edge()

#browser = webdriver.Firefox()
browser.maximize_window()

#starting our search engine
browser.get(search_engine)

#searching for element 'q' - it's a place for typing search request
element = browser.find_element_by_name('q')

#sending our search string, adding to it a word ' wiki' and finishing by sending RETURN
element.send_keys(search_string + ' wiki' + Keys.RETURN)

#waiting for loading SERP
browser.implicitly_wait(5)

#searching for link on Wikipedia page and emulating clicking to it
wiki_link = browser.find_element_by_xpath("//*[contains(text(), 'Wiki')]")
wiki_link.click()

#waiting for complete loading
browser.implicitly_wait(15)

#then return to start page and waiting for complete loading
browser.back()
browser.implicitly_wait(20)

#searching for all links in SERP
all_links = browser.find_elements_by_css_selector('a:link')
hrefs = []
hrefs = [x.get_attribute('href') for x in all_links if x.get_attribute('href') not in hrefs]

#loading a new page by randomly choosed link and staying there for 120-180 seconds
other_link = hrefs[random.randint(0, 10)]
browser.get(other_link)
browser.implicitly_wait(random.randint(120, 180))

#finish!
browser.quit()
