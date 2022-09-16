from selenium import webdriver

PATH = "H:\Data Analyst Projects\Web-Scrapping-with-Python\Web-Scraping-uisng-Selenium\chromedriver.exe"
driver = webdriver.Chrome(PATH)


driver.get("https://techwithtim.net")

driver.close()