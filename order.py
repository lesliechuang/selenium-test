from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException

#加载页面
def load():
    try:
        #可以将driver的路径配置到环境变量中，下面就不要在些路径
        #使用78版本的chrome
        browser = webdriver.Chrome('lib/chromedriver.exe')
        #打开京东首页
        browser.get('https://www.jd.com/')
        return browser
    except TimeoutException:
        print('加载页面超时') 

#搜索商品
def search(browser):
    try:
        #找到搜索输入框
        input = browser.find_element_by_id('key')
        #清空输入框
        input.clear()
        #输入搜索字段
        input.send_keys(u"逍客")
        #找到搜索按钮
        button = browser.find_element_by_xpath('//div[@id="search"]//button[@clstag="h|keycount|head|search_a"]')
        #点击搜索
        button.click()
    except NoSuchElementException:
        print('search找不到元素')

#添加购物车
def addToCart(browser):
    try:
        #判断页面元素已经加载完成，如果觉得页面加载非常快，可以不判断
        wait = WebDriverWait(browser,10)
        glist = wait.until(EC.presence_of_element_located((By.ID,'J_goodsList')))
        #找到我想选择的商品连接，并点击
        goodslink = browser.find_element_by_xpath('//div[@id="J_goodsList"]//ul//li[@data-pid="32266699012"]//div[@class="p-name p-name-type-2"]//a')
        goodslink.click()
        #转到打开的商品详情页面
        browser.switch_to_window(browser.window_handles[1])
        btn = wait.until(EC.presence_of_element_located((By.ID,'choose-btns')))
        #增加一个商品数目
        addCountLink = browser.find_element_by_xpath('//div[@id="choose-btns"]//a[@class="btn-add"]')
        addCountLink.click()
        #加入购物车
        addCartLink = browser.find_element_by_id('InitCartUrl')
        addCartLink.click()
    except NoSuchElementException:
        print('addToCart找不到元素')

if __name__ == '__main__':
    browser = load()
    search(browser)
    addToCart(browser)
    time.sleep(10)