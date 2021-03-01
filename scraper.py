"""Defining the crawler of parsing out the images from the
given website.
:return: Images of the fruits form the websites
"""
from selenium import webdriver
from bs4 import BeautifulSoup
import threading
import sys


def image_spider(input_field):
    url = "https://pixabay.com/images/search/"
    browser = webdriver.Chrome(executable_path="C:\\Users\\ABHAY\\Documents\\chromedriver.exe")
    if len(sys.argv) > 1:
        input_field = ' '.join(sys.argv[1:])
    else:
        productsImg = []
        func = lambda adder: browser.get(adder)
        while productsImg is []:
            thread = threading.Thread(target=func, args=url + input_field)
            thread.start()
        # time.sleep(8)
        func(adder=url + input_field)
        page_source = browser.page_source
        soup = BeautifulSoup(page_source, features="html.parser")
        productsImg.append(page_source)
        browser.quit()
        image_link = []
        title = []
        picture = []
        images = soup.findAll('img')
        for image in images:
            image_link.append(image['src'])
        for alt in images:
            if len(title) == 16:
                break
            try:
                title.append(alt['alt'])
            except KeyError:
                continue
        for il in image_link:
            if '.jpg' not in il:
                continue
            picture.append(il)
        return picture, title

# And Done
