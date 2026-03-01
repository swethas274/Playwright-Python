from playwright.sync_api import Page, expect

def test_navigation(page: Page):
    page.goto("https://example.com")
    expect(page).to_have_title("Example Domain")
    
def test_click(page: Page):
    page.goto("https://playwright.dev/")
    page.get_by_role("link", name="Get Started").click()
    expect(page).to_have_url("https://playwright.dev/docs/intro")
    
def test_fill(page: Page):
    page.goto("https://demoqa.com/text-box")
    page.locator("#userName").fill("Swetha")
    page.locator("#userEmail").fill("a@g.com")
    
from playwright.sync_api import Page, expect

def test_check(page: Page):

    page.goto("https://www.testmuai.com/selenium-playground/checkbox-demo/")

    # locate checkbox using its label text
    checkbox = page.get_by_label("Click on check box")

    # check it
    checkbox.check()

    # verify
    expect(checkbox).to_be_checked()

    # proof
    page.screenshot(path="checkbox_success.png")

    print("✅ Checkbox checked successfully")
    
def test_hover(page: Page): 
    page.goto("https://demoqa.com/tool-tips")
    page.locator("#toolTipButton").hover()

def test_focus(page: Page):
    page.goto("https://demoqa.com/text-box")
    page.locator("#userName").focus()
    
def test_press(page: Page):
    page.goto("https://demoqa.com/text-box")
    input_box=page.locator("#userName")
    input_box.fill("Swetha")
    input_box.press("Enter")
    
def test_select_option(page: Page):
    page.goto("https://demoqa.com/select-menu")
    page.locator("#oldSelectMenu").select_option("Red")  #Selects the option 
