from selenium import webdriver
import datetime
import time
import telegram_send
import os

os.system('printf "1782618485:AAGk6TxOkq0FyW7YWlpDu5lo3aAnszd_uDM\npub\nt.me/amazPT" | telegram-send --configure-channel')

def get_driver():
    """Start web driver"""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.implicitly_wait(10)
    return driver


# chromeWebDriverPath = './chromedriver'
priceXPath = '//*[@id=\"priceblock_ourprice\"]'

# driver = webdriver.Chrome(chromeWebDriverPath)
driver = get_driver()
productFile = open('products.txt', 'r')
Lines = productFile.readlines()

outputFile = open('prices.txt', 'a')
telegram_send.send(messages=["deployed model..."])
while True:
    for line in Lines:
        productName = line.split('@')[0]
        productUrl = line.split('@')[1]
        productThresh = line.split('@')[2]
        driver.get(productUrl)
        element = driver.find_element_by_xpath(priceXPath)
        price = element.text.split(' ')[1]
        if price <= productThresh:
            telegram_send.send(messages=[str(productName) + ': ' + str(price)])
        print(productName, price)
        outputFile.write(str(datetime.datetime.now()) + ': ' + productName+'@'+price+'\n')
    time.sleep(10)

productFile.close()
outputFile.close()
driver.close()

