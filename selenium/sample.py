#! /usr/bin/env python3
import requests
from selenium import webdriver
d = '/Users/jhu/Downloads/chromedriver'

driver = webdriver.Chrome(executable_path=d)
driver.get("http://zbox.unservice.net/zentao/my/")
#driver.switch_to_frame('login-panel')
driver.find_element_by_id("account").send_keys('huj')
driver.find_element_by_name("password").send_keys('qwe321')
driver.find_element_by_id("submit").click()

#driver.switch_to_window(driver[0])
#driver.get("http://zbox.unservice.net/zentao/project-task.html")
driver.implicitly_wait(1)
cookies = driver.get_cookies()
driver.find_element_by_link_text('项目').click()
#print(driver.page_source)
driver.find_element_by_id('currentItem').click()
driver.implicitly_wait(1)
#time.sleep(1)
#driver.find_element_by_xpath('//*[@id="createActionMenu"]/a').click()
driver.find_element_by_xpath('//*[@id="search"]').send_keys('[PJM]90.临时需求')
driver.find_element_by_link_text('[PJM]90.临时需求').click()
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="taskTree"]/div/div/div[2]/ul/li[1]/i').click()
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="module1201"]').click()
#driver.find_element_by_link_text('[PJM]02.数据中心').click()
# driver.quit()
#
jar = requests.cookies.RequestsCookieJar()
for c in cookies:
    jar.set(c['name'],c['value'])

req_head={
    "User-Agent":"Mozilla/5.0· (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
}

s = requests.Session()
response = s.get('http://zbox.unservice.net/zentao/project-task-88-byModule-1201.html', headers=req_head,cookies=jar)
print(response.text)
#
