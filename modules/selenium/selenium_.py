import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Chrome Options: https://peter.sh/experiments/chromium-command-line-switches/

ROOT = Path(__file__).parent
DRIVER = ROOT / 'drivers' / 'chromedriver.exe'

TIME_TO_WAIT = 10


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(executable_path=str(DRIVER))

    chrome_browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options,
    )

    return chrome_browser


options = ()
browser = make_chrome_browser(*options)

browser.get('https://www.google.com')

# waits to find the search input
search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
    EC.presence_of_element_located((By.NAME, 'q'))
)

# sending a query
search_input.send_keys('Hello World!')
search_input.send_keys(Keys.ENTER)

# colecting query result
results = browser.find_element(By.ID, 'search')

# getting the links from the result
links = results.find_elements(By.TAG_NAME, 'a')

# selecting first link
links[0].click()
time.sleep(5)
