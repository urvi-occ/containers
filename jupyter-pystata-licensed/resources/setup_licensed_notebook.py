from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import os


opts = Options()
opts.headless = True
browser = webdriver.Firefox(options=opts)


print("Loading jupyterlab...")
browser.get("http://127.0.0.1:8888/lw-workspace/proxy/notebooks")
time.sleep(2)

print("Reading .lic file")
with open("/usr/local/stata17/stata.lic", "r") as lic_file:
    print("Found stata.lic file")

print("Ready to open notebook")
element = browser.find_element(By.LINK_TEXT, "licensed_stata_session.ipynb")
actions = ActionChains(browser)
actions.click(on_element = element)
actions.perform()
print("Notebook is opened")

actions.pause(5)

# Down-arrow to get to the second cell in the notebook
actions.send_keys(Keys.DOWN)
actions.pause(1)
actions.perform()

# Run the stata setup cell
print("Ready to run stata setup cell")
actions.key_down(Keys.SHIFT)
actions.send_keys(Keys.ENTER)
actions.key_up(Keys.SHIFT)
actions.perform()
actions.pause(5)

# Save notebook with output
print("Ready to save notebook")
actions.key_down(Keys.CONTROL)
actions.send_keys("S")
actions.key_up(Keys.CONTROL)
actions.pause(1)
actions.send_keys(Keys.ENTER)
actions.perform()
