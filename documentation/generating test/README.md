## 📂 Generating Tests using Playwright Codegen

Playwright provides a built-in tool called **Codegen** that helps automatically generate test scripts by recording user interactions in the browser.

This feature is useful for:
- Learning Playwright faster
- Generating accurate locators
- Understanding page structure
- Creating initial test templates

---

### ▶️ Running Codegen

Start recording by running:

```bash
playwright codegen https://example.com
```

This will:
- Open a browser window
- Start recording your actions
- Generate Playwright test code automatically

### Recording a Test using Codegen

While the browser is open:

- Navigate through the website normally.
- Click buttons, fill forms, or interact with elements.
- Playwright records every action automatically.
- Generated code appears in real time inside the Codegen window.

### Generating Locators

Codegen automatically suggests best-practice locators such as:

- get_by_role()
- get_by_label()
- get_by_text()

