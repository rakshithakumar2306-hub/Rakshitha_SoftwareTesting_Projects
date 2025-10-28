from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=800)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")

    # Login
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    time.sleep(2)

    page.get_by_text("Sauce Labs Backpack").click()
    page.locator("button:has-text('Add to cart')").click()

    page.locator(".shopping_cart_link").click()
    page.locator("#checkout").click()

    page.fill("#first-name", "Rita")
    page.fill("#last-name", "S")
    page.fill("#postal-code", "570001")
    page.locator("#continue").click()
    time.sleep(2)

    # Screenshot
    page.screenshot(path="checkoutSwagLab.png")

    time.sleep(2)
    browser.close()
