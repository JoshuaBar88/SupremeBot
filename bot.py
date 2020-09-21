from selenium import webdriver
#from helper import keys
import multiprocessing
import aiohttp
import asyncio
from requests_futures import sessions
from bs4 import BeautifulSoup as soup
#import string
import time
#from bs4.element import Tag as bs_tag
#from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#import requests



async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.content.read()

def order(k):
    #results3 = bs_tag
    options = webdriver.ChromeOptions()
    #options.add_argument('--app')
    options.add_experimental_option("excludeSwitches", ['enable-automation']);

    options.add_argument('--window-size=100,520')

    driver = webdriver.Chrome(executable_path="/Users/joshuabarnett/.wdm/drivers/chromedriver/80.0.3987.106/mac64/chromedriver", options = options)
    list1=[]
    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(get("https://www.supremenewyork.com/shop/all/t-shirts"))]
    loop.run_until_complete(asyncio.wait(tasks))
    #print("Results: %s" % [task.result() for task in tasks])
    list1.append([task.result() for task in tasks])
    opp = soup(str(list1[0][0]), "html.parser")
    money = []
    results2 = opp.find_all('div', attrs={'class': 'inner-article'})
    
    for i in results2:
        p = str(i)
        if "Small Box" in p and "White" in p:
            #print(k)
            finder = i.contents[1]
            #print(finder)
            results3 = finder.find('a', attrs={'class': 'name-link'})
            #print(type(results3))
            break
    
    try:
        gang = "https://www.supremenewyork.com"+str(results3.get('href'))
    except UnboundLocalError:
        driver.close()
    driver.get(gang)
    driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
    time.sleep(.40)
    driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
    driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(k["name"])
    driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(k["email"])
    driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(k["phone"])
    driver.find_element_by_xpath('//*[@id="bo"]').send_keys(k["address"])
    driver.find_element_by_xpath('//*[@id="oba3"]').send_keys(k["otherA"])
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="rnsnckrn"]').send_keys(k["cards"])
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(k["zip"])
    driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(k['city'])
    
    #driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(k["cvv"])
    driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()
    driver.find_element_by_xpath('//*[@id="order_billing_state"]/option[55]').click()
    driver.find_element_by_xpath('//*[@id="credit_card_month"]/option[4]').click()
    driver.find_element_by_xpath('//*[@id="credit_card_year"]/option[4]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="pay"]/input').click()


if __name__ == '__main__':
    #options = webdriver.ChromeOptions()
    #options.add_argument('--disable-images')
    #driver = webdriver.Chrome(executable_path="/Users/joshuabarnett/.wdm/drivers/chromedriver/80.0.3987.106/mac64/chromedriver", options = options)
    #driver = webdriver.Chrome(ChromeDriverManager().install()) 
 
    keys = {
    "name": "Joshua Barnett",
    #"url": "4447962409932096",
    "email": "ti.joshuabarnett@gmail.com",
    "phone": "347-972-6340",
    "address": "76 Limestone Way",
    "zip": "22406",
    "otherA": "",
    "cards": "4789751001074563",
    "cvv": "693",
    "city": "Fredericksburg"
    } 
    for i in range(2):
        p = multiprocessing.Process(target= order, args=(keys, ))
        p.start()
        #p.join()
    

