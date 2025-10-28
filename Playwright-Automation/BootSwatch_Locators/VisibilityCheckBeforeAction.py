from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,slow_mo=2000)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")
    x=page.get_by_role("button", name="Default Button")
    if x.is_visible():
        x.highlight()
        x.click()
    else:
         print("No default button found")
    page.screenshot(path="./VisibilityCheck.png")
    browser.close()