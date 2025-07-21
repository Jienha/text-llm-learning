
# Selenium Web Driver script:

from selenium import webdriver # provides all the WebDriver implementations.
from selenium.webdriver.common.keys import Keys # provide keys in the keyboard like RETURN, F1, ALT etc.
from selenium.webdriver.common.by import By # used to locate elements within a document

# instance of Firefox WebDriver is created.
driver = webdriver.Firefox()

# .get method will navigate to a page given by the URL
driver.get("http://www.python.org")
# WebDriver will wait until the page has fully loaded 
# before returning control to your test or script.
# (Be aware that if your page uses a lot of AJAX 
# on load then WebDriver may not know when it has 
# completely loaded)

# The next line is an assertion to confirm that title has the word “Python” in it
assert "Python" in driver.title

# WebDriver offers a number of ways to find elements using the find_element method
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()