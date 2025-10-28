from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    iphone = p.devices['iPhone 14']          # Pick a device
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(**iphone)  # Use the device
    page = context.new_page()
    page.goto("https://bootswatch.com")         # Open website
    page.screenshot(path="iphone_screenshot.png")  # Take screenshot
    browser.close()
