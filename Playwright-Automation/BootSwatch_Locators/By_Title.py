import time

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")

    x=page.get_by_title("Source").nth(0)
    x.highlight()
    x.click()
    time.sleep(5)
    browser.close()


