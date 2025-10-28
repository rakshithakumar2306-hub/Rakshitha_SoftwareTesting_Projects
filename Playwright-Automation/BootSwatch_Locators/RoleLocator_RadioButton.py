

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")
    x = page.get_by_role("radio", name="Option one is this and that—be sure to include why it's great")
    x.highlight()
    page.screenshot(path="./screenshot.png", full_page=True)
    x.click()
    browser.close()


