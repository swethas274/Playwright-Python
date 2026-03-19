import asyncio
from playwright.async_api import async_playwright
from urllib.parse import urlparse
import os
import sys

INPUT_FILE = "input.txt"

# 🔥 Get script name dynamically
script_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
OUTPUT_DIR = os.path.join("tmp", script_name)

os.makedirs(OUTPUT_DIR, exist_ok=True)

def clean_url(line):
    # take only first part (remove status codes etc.)
    url = line.strip().split()[0]

    # add scheme if missing
    if not url.startswith("http"):
        url = "http://" + url

    return url

def sanitize_filename(url):
    try:
        parsed = urlparse(url)
        name = parsed.netloc.replace(":", "_")

        if not name:
            name = url.replace("http://", "").replace("https://", "").replace("/", "_")

        return os.path.join(OUTPUT_DIR, name + ".png")

    except Exception:
        return os.path.join(OUTPUT_DIR, "invalid.png")

async def capture():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(ignore_https_errors=True)

        with open(INPUT_FILE, "r") as f:
            lines = [line.strip() for line in f if line.strip()]

        for line in lines:
            url = clean_url(line)
            page = await context.new_page()

            try:
                print(f"[+] Opening {url}")
                await page.goto(url, timeout=15000, wait_until="domcontentloaded")
                await page.wait_for_timeout(2000)

            except Exception as e:
                print(f"[!] Load error: {url} -> {e}")

            try:
                filename = sanitize_filename(url)
                await page.screenshot(path=filename, full_page=True)
                print(f"[✓] Saved: {filename}")

            except Exception as e:
                print(f"[!] Screenshot failed: {url} -> {e}")

            await page.close()

        await browser.close()

asyncio.run(capture())