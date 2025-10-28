import time

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=1000)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")

    #b= page.locator(".btn.btn-primary")
    b = page.get_by_role("button", name="Primary", exact=True).nth(0)
    b.highlight()
    b.click()

    page.screenshot(path="./Task3.png")

    browser.close()
