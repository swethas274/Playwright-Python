## Commands and its use
1) `sync_api` : 1 step at a time
2) `async_api` : many things simultaneously
3) `page.goto(url)` : goes to the site
4) `page.click(button)` : clicks button
5) `page` : one browser tab 
6) `expect` : checker *eg: expect(page).to_have_title("asdf")* `expect(THING).check_condition()`
7) `re.complie()` : pattern match
8) `page.get_by_role()` : find a clickable link whose visible test is mentioned *eg:page.get_by_role("link,name="title")*
9) `page.screenshot(path="x.png")` - saves a screenshot in this path
10) `pytest --headed -s` : screening
11) `pytest --headed --screenshot=only-on-failure` : if test fail then screen shots automatically 
12) `pytest --headed --video=on` : video of the test saved on test-result/

## Basic Action comands
| Command                   | Human Meaning        |
| ------------------------- | -------------------- |
| `page.goto()`             | open website         |
| `locator.click()`         | click element        |
| `locator.fill()`          | type text            |
| `locator.check()`         | tick checkbox        |
| `locator.hover()`         | move mouse over      |
| `locator.focus()`         | place cursor         |
| `locator.press()`         | press keyboard key   |
| `locator.select_option()` | choose dropdown item |
