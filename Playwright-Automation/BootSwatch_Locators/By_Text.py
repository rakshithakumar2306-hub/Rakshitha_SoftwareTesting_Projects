
import time

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")

    x =  page.get_by_text("Submit").first
    x.highlight()
    x.click()
    time.sleep(3)

    page.goto("https://www.facebook.com/r.php?entry_point=login")
    x = page.get_by_text("Sign Up", exact=True).first
    x.highlight()
    time.sleep(2)
    x.click()
    time.sleep(2)
    browser.close()


