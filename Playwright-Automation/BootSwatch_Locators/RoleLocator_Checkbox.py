from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto("https://bootswatch.com/default/")
    x = page.get_by_role("checkbox", name="Default checkbox")
    x.highlight()
    print("Checkbox is checked:", x.is_checked())
    page.screenshot(path="./screenshot.png", full_page=True)
    x.click()
    x.check()
    print("Checkbox is checked:", x.is_checked())
# page.get_by_role("link", name="Sign up").click()

"""
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    y = page.get_by_role("checkbox", name="checkbox 1")
    print("Checkbox is checked:", y.is_checked())
    y.check()
    print("Checkbox is checked:", y.is_checked())
    browser.close()

"""
