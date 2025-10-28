import time

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=2000)
    page = browser.new_page()
    page.goto("https://www.swiggy.com/search/")


    ice_cream= page.get_by_placeholder("Search for restaurants and food")
    ice_cream.fill("Classic Death by Chocolate")
    ice_cream.highlight()
    ice_cream.click()
    time.sleep(2)

    x= page.get_by_test_id("autosuggest-item").nth(0)
    x.highlight()
    time.sleep(2)
    x.click()
    page.wait_for_timeout(3000)


    page.locator(".sc-ggpjZQ.sc-cmaqmh.jTEuJQ.fcfoYo.add-button-center-container").click()
    time.sleep(6)
    checkout=page.get_by_role("link", name="Cart")
    checkout.highlight()
    checkout.click()
    time.sleep(5)
    page.screenshot(path="./checkout.png")


    y=page.get_by_text("LOG IN", exact=True)
    y.highlight()
    y.click()
    time.sleep(3)