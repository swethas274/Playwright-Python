# 📸 Automated Website Screenshot Tool (Playwright)

## 🔍 Overview

This project is a lightweight **recon automation tool** built using Playwright and Python. It reads a list of URLs (such as subdomains discovered during reconnaissance), visits each one, and captures a **full-page screenshot** — regardless of HTTP status (200, 403, 500, etc.).

This is especially useful in **bug bounty hunting, penetration testing, and asset discovery**, where quickly visualizing large numbers of targets helps identify high-value entry points.

---

## 🎯 Purpose

During reconnaissance, tools like `httpx`, `subfinder`, or `amass` generate large lists of domains. Manually visiting each one is slow and inefficient.

This script automates that process by:

* Opening each URL in a real browser (Chromium)
* Rendering the page (even if partially broken)
* Capturing a screenshot
* Saving it in an organized folder structure

---

## 👥 Who Can Use This?

This tool is useful for:

* 🐞 Bug bounty hunters
* 🔐 Security researchers
* 🧑‍💻 Penetration testers
* 🌐 Web developers auditing large systems
* 🧪 Anyone performing web reconnaissance

---

## ⚙️ Features

* ✅ Captures screenshots even for **403 / 500 / broken pages**
* ✅ Supports messy input files (e.g., `httpx` output with status codes)
* ✅ Automatically adds `http://` if missing
* ✅ Saves output in structured folders: `tmp/<script_name>/`
* ✅ Handles SSL issues (`ignore_https_errors`)
* ✅ Works with JavaScript-heavy websites

---

## 📂 Input Format

The script accepts a file containing URLs or domains.

Example:

```
https://example.com
sub.domain.com 403
test.site.org
```

It automatically cleans and processes each line.

---

## 📸 Output

Screenshots are saved in:

```
tmp/<script_name>/
```

Example:

```
tmp/script1/
├── example.com.png
├── sub.domain.com.png
├── test.site.org.png
```

---

## 🚀 Installation

### 1. Install dependencies

```
pip install playwright
playwright install
```

---

## ▶️ Usage

Run the script:

```
python script1.py
```

---

## 🧠 How It Works

1. Reads each line from the input file
2. Cleans and normalizes the URL
3. Launches a headless Chromium browser
4. Visits the page (`domcontentloaded` for speed & reliability)
5. Captures a full-page screenshot
6. Saves it using the domain name

Even if the page fails to load completely, the script still attempts a screenshot.

---

## 🔥 Example Use Case

You run `httpx` and get 500+ subdomains.

Instead of opening each manually:

* Run this script
* Review screenshots visually
* Quickly identify:

  * Login portals 🔐
  * Admin dashboards ⚙️
  * Debug/error pages ⚠️
  * Interesting attack surfaces 🎯

---

## ⚠️ Disclaimer

This tool is intended for **authorized security testing and educational purposes only**.
Do not use it on systems without proper permission.

---

## 🚀 Future Improvements (Optional Ideas)

* Parallel processing (faster execution)
* Auto-classification (login/admin/error pages)
* Integration with recon tools (httpx, nuclei)
* Screenshot comparison (detect changes over time)

---

## 💡 Final Note

This tool is a small but powerful step toward building a **full recon pipeline**.
Used correctly, it can save hours of manual work and help you spot vulnerabilities faster.

---
