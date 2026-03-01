from playwright.sync_api import Page, expect
import re  

def test_title(page: Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))  #Allows partial title matching.
    
def test_url(page: Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_url(re.compile("playwright.dev"))
    
# the below code snippet have a pivot position in old tab and moves to the found url to new tab so it causes an error 
# so we need to make it like click link -> open new tab -> capture the tab -> switch control -> assertl url
def test_url_in_page(page: Page):
    page.goto("https://playwright.dev/")
    with page.context.expect_page() as new_page_info:
        page.get_by_role("link", name="Github repository").click()
        
    new_page=new_page_info.value #capture the new page object
    
    expect(new_page).to_have_url(re.compile("github.com/microsoft/playwright"))

def test_checkbox_assert(page: Page):
    page.goto("https://www.testmuai.com/selenium-playground/checkbox-demo/")
    checkbox=page.get_by_label(re.compile("Click on check box"))
    checkbox.check()
    expect(checkbox).to_be_checked()
    
def test_text(page: Page):
    page.goto("https://example.com/")
    expect(page.locator("h1")).to_have_text("Example Domain")
    