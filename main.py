from selenium import webdriver

chromeWebDriverPath = '/Users/manish.karna/Downloads/chromedriver'
priceXPath = '//*[@id=\"priceblock_ourprice\"]'

driver = webdriver.Chrome(chromeWebDriverPath)

productFile = open('products.txt', 'r')
Lines = productFile.readlines()

outputFile = open('prices.txt', 'w')

for line in Lines:
    productName = line.split('@')[0]
    productUrl = line.split('@')[1]
    driver.get(productUrl)
    element = driver.find_element_by_xpath(priceXPath)
    price = element.text.split(' ')[1]
    print(productName, price)
    outputFile.write(productName+'@'+price+'\n')

productFile.close()
outputFile.close()
driver.close()