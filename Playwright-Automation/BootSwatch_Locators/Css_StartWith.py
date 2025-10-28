import time

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("https://www.amazon.in/")
    page.locator("input[id^='twotab']").fill("Iphone 13 pro max")
    page.locator("input[id=nav-search-submit-button]").click()
    time.sleep(3)
    browser.close()


