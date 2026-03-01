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
    
    
'''
1) visibility => expect(page.get_by_role("button")).to_be_visible()
2) checked => expect(heckbox).to_be_checked()
3) enabled => expect(page.get_by_role("button")).to_be_enabled()
4) text => expect(page.locator("h1")).to_have_text("Example Domain")
5) url => expect(page).to_have_url(re.compile("playwright.dev"))
6) partial text => expect(page.locator("h1")).to_contain_text("Example")
7) title => expect(page).to_have_title(re.compile("Playwright"))
8) attribute => expect(page.locator("input")).to_have_attribute("type", "text")
9) class => expect(page.locator("button")).to_have_class(re.compile("primary"))
10) value => expect(page.locator("input")).to_have_value("Hello")
11) count => expect(page.locator("li")).to_have_count(5)
12) visible => expect(page.locator("button")).to_be_visible()
13) hidden => expect(page.locator("button")).to_be_hidden()
14) editable => expect(page.locator("input")).to_be_editable()
15) disabled => expect(page.locator("button")).to_be_disabled()
16) focused => expect(page.locator("input")).to_be_focused()
17) selected => expect(page.locator("option")).to_be_selected()
18) checked => expect(page.locator("input[type='checkbox']")).to_be_checked()
19) unchecked => expect(page.locator("input[type='checkbox']")).not_to_be_checked()
20) empty => expect(page.locator("input")).to_be_empty()
21) input value => expect(page.locator("input")).to_have_value("Hello")
'''