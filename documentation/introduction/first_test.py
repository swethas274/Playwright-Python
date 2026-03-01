import re
from playwright.sync_api import Page, expect
'''
Page → browser tab object
expect → assertion system
'''

def test_has_title(page: Page):
    '''
    test_ prefix → pytest auto-detects test
    page → automatically injected fixture by Playwright
    '''
    
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))  #Allows partial title matching.
    
def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")
    page.get_by_role("link", name="Get Started").click()
    
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()