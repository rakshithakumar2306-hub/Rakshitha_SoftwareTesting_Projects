import time

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("https://www.facebook.com/r.php?entry_point=login")
    x = page.locator("//input[@name='firstname']")
    x.fill("John")
    x.highlight()
    time.sleep(2)

    browser.close()


