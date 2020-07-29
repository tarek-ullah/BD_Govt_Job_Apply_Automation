from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()  

#Clicking apply now button 

driver.get("http://btrc.teletalk.com.bd/") 
#time.sleep(1)
driver.find_element_by_xpath("//a[contains(text(),'Apply Now')]").click()
#time.sleep(1)

# Clicking AD post to apply
driver.get("http://btrc.teletalk.com.bd/index.php?action=job-list")
driver.find_element_by_xpath("//a[contains(text(),'Assistant Director ( Technical ) (Grade-9)')]").click()
#time.sleep(1)

driver.get("http://btrc.teletalk.com.bd/form.php?post_id=167")
print(driver.title)
#search_bar = driver.find_element_by_name("q")
#search_bar = driver.find_element_by_xpath("//input[@id='id-search-field']")
#Applicants name fill in
search_bar = driver.find_element_by_xpath("//input[@id='persoanl_info_applicants_name']")
search_bar.clear()
search_bar.send_keys("H. M. TAREK ULLAH")

# Fathers name fill in 
search_bar_father =  driver.find_element_by_xpath("//input[@id='persoanl_info_fathers_name']")
search_bar_father.clear()
search_bar_father.send_keys("MD. ABDUL MALEK")

# Mothers name fill in 
search_bar_mother = driver.find_element_by_xpath("//input[@id='persoanl_info_mothers_name']")
search_bar_mother.clear()
search_bar_mother.send_keys("TAHMINA KHATUN")
search_bar_mother.send_keys(Keys.RETURN)("")
print(driver.current_url)
driver.close()



