from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://inventwithpython.com')
linkElem = browser.find_element_by_link_text('Read Online for Free')
type(linkElem)
linkElem.click()