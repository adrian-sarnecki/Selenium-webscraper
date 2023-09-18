from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

wd_path = "A:\Programowanie\Projekty\Python\Selenium-webscraper\chromedriver.exe"  # path to chromedriver, remember to choose your own

options = Options()
options.add_experimental_option("detach", True)
service = Service(executable_path=wd_path)
driver = webdriver.Chrome(service=service, options=options)
