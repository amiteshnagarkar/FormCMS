from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
driver.get('http://127.0.0.1:8000/employee/')


driver.implicitly_wait(10)


fullnamebox = driver.find_element_by_xpath('//*[@id="id_fullname"]')
driver.implicitly_wait(3)
fullnamebox.send_keys('Vikram Nagarkar')

mobilebox = driver.find_element_by_xpath('//*[@id="id_mobile"]')
driver.implicitly_wait(3)
mobilebox.send_keys('999')

empbox = driver.find_element_by_xpath('//*[@id="id_emp_code"]')
driver.implicitly_wait(3)
empbox.send_keys('678')

#positionbutton = driver.find_element_by_xpath('//*[@id="id_position"]')
#positionbutton.click()

select = Select(driver.find_element_by_id('id_position'))
select.select_by_value('4')
driver.implicitly_wait(3)

chooseFile = driver.find_element_by_id("id_image")
chooseFile.send_keys('/Users/amiteshnagarkar/IMG_2719 copy.png')




submitbutton = driver.find_element_by_xpath('/html/body/div/div/div/form/div[4]/div[1]/button')

submitbutton.click()
