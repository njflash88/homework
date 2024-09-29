from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
 
service_obj = Service('./chromedriver')
driver = webdriver.Chrome(service=service_obj)

### work #1
print("************* work#1 started **********")
url = "https://hk.on.cc/hk/bkn/cnt/news/20240928/bkn-20240928130520134-0928_00822_001.html"
driver.get(url)
para = driver.find_element(By.XPATH,("//div[@class='breakingNewsContent']")).text
print(para)
time.sleep(3)
print("************* work#1 ended **********")
###  end work #1

### work#2
print("************* work#2 started **********")
url = "https://www.ibm.com/thought-leadership/institute-business-value/report/technology-sustainability-responsible-computing"
driver.get(url)
search1 = driver.find_element(by=By.CSS_SELECTOR, value="body > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > main:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > h3:nth-child(7)").text
print(search1)
time.sleep(3)
print("************* work#2 ended **********")
### end work#2



### work #3
print("************* work#3 started **********")
url = "https://hk.news.yahoo.com/%E6%97%85%E5%B1%85%E6%9D%B1%E4%BA%AC%E4%B8%8A%E9%87%8E%E5%8B%95%E7%89%A9%E5%9C%92%E5%A4%A7%E7%86%8A%E8%B2%93%E5%8A%9B%E5%8A%9B%E5%92%8C%E7%9C%9F%E7%9C%9F%E6%9C%80%E5%BE%8C-%E6%97%A5%E8%88%87%E9%81%8A%E5%AE%A2%E8%A6%8B%E9%9D%A2-084220623.html"
driver.get(url)
para = driver.find_element(By.XPATH,"//div[@id='caas-art-1019c6aa-0e80-37d3-90c7-3cc1f3a705ad']").text
print(para)
time.sleep(3)
print("************* work#3 ended **********")

###  end work #3

driver.close()
