from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=2000)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")
    x=page.get_by_role("link", name="Default")
    x.highlight()
    page.screenshot(path="./linkInteraction.png")
    x.click()
    browser.close()