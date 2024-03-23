from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import *
import sys
def getSellingRate(date,Currency):
    try:
        driver = webdriver.Chrome()
        driver.implicitly_wait(1)

        #使用货币代码，从英文页面爬取
        driver.get("https://www.boc.cn/sourcedb/whpj/enindex2.htm")
        driver.switch_to.frame('DataList')

        #set startDate,endDate,Currency
        driver.find_element(By.XPATH,'//*[@id="historysearchform"]/input[1]').send_keys(date)
        driver.find_element(By.XPATH,'//*[@id="historysearchform"]/input[2]').send_keys(date)
        Select(driver.find_element(By.XPATH,'//*[@id="historysearchform"]/select')).select_by_value(Currency)

        driver.find_element(By.XPATH,'//*[@id="historysearchform"]/input[3]').click()
        sellingRate=driver.find_element(By.XPATH,'/html/body/table[2]/tbody/tr[2]/td[5]').text
        with open("result.txt", 'w') as file:
            file.write(sellingRate)
            print(date+Currency+"现汇卖出价为"+sellingRate+"已写入result.txt")
    except NoSuchElementException:
        print("请检查日期与货币代码格式，若无误则当日无数据")
    except WebDriverException:
        print("请检查互联网连接或Chrome webdriver配置")
    finally:
        driver.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("请输入两个参数:日期 货币代码");
    else:
        getSellingRate(sys.argv[1],sys.argv[2])

