import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import Keys

driver = webdriver.Chrome()
doc_id = input("Doc ID: ")

try:
    driver.get("https://docs.google.com/document/d/" + doc_id)


finally:
    driver.quit()
