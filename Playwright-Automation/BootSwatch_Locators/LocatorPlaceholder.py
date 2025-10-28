import time

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=1000)
    page = browser.new_page()
    page.goto("https://demo.playwright.dev/todomvc/")

    input_box=page.get_by_placeholder("What needs to be done?")
    input_box.highlight()
    input_box.fill("Learn Locators")
    input_box.click()
    #time.sleep(3)

    cbox=page.get_by_role("checkbox").nth(0)
    cbox.highlight()
    cbox.click()
    time.sleep(3)
    page.screenshot(path="./Checkbox.png")

    browser.close()
