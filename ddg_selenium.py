from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get('https://duckduckgo.com')

assert 'DuckDuckGo' in driver.title
search_box = driver.find_element(By.ID,'search_form_input_homepage')
search_button = driver.find_element(By.ID, 'search_button_homepage')
search_box.click()
search_box.send_keys('hello world!')
search_button.click()

link = driver.find_element(By.ID, 'r1-0')
link.click()

driver.quit()