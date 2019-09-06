from selenium import webdriver
import hashlib
driver = webdriver.Chrome("./chromedriver.exe")
base_url = "http://docker.hackthebox.eu:56165"
driver.get(base_url)
md5 = driver.find_element_by_xpath("/html/body/h3").text
md5 = hashlib.md5(md5.encode())
driver.find_element_by_name("hash").send_keys(md5.hexdigest())
driver.find_element_by_xpath("/html/body/center/form/input[2]").click()
