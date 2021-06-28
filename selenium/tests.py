from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



# print("sample test case started")  
# driver = webdriver.Chrome(r"C:\Users\Mide\Documents\django-work\blog\myblog\selenium\browsers\chromedriver.exe")  
# #driver=webdriver.firefox()  
# #driver=webdriver.ie()  
# #maximize the window size  
# driver.maximize_window()  
# #navigate to the url  
# driver.get("http://127.0.0.1:8000/")  
# #identify the Google search text box and enter the value  
# driver.find_element_by_name("q").send_keys("javatpoint")  
# time.sleep(3)  
# #click on the Google search button 
# driver.find_element_by_name("btnK").send_keys(Keys.ENTER) 
# # driver.find_element_by_name("btnK").send_keys(Keys.ENTER)  
# time.sleep(3)  
# #close the browser  
# driver.close()  
# print("sample test case successfully completed")  



print("sample test case started")  
driver = webdriver.Chrome(r"C:\Users\Mide\Documents\django-work\blog\myblog\selenium\browsers\chromedriver.exe")  
#driver=webdriver.firefox()  
#driver=webdriver.ie()  
#maximize the window size  
driver.maximize_window()  
#navigate to the url  
driver.get("http://127.0.0.1:8000/")  
#identify the Google search text box and enter the value  
driver.find_element_by_xpath("//a[contains(text(),'Blog')]").click()  
time.sleep(3)  
#click on the news
driver.find_element_by_xpath("//a[contains(text(),'Maybe Joeboy’s Album Isn’t That Bad After All')]").click()  

# driver.find_element_by_name("btnK").send_keys(Keys.ENTER)  
time.sleep(5) 
# make a comment
driver.find_element_by_name("name").send_keys("Alatise Gbenga") 
driver.find_element_by_name("email").send_keys("mide999@gmail.com") 
driver.find_element_by_name("body").send_keys("A very good album, I recommend") 
driver.find_element_by_xpath("//body/div[1]/form[1]/p[1]/input[1]").click()
time.sleep(9) 
#close the browser  
driver.close()  
print("sample test case successfully completed")  




