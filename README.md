## Project Overview

This repository documents my learning and experimentation with **Playwright using Python** for browser automation and end-to-end testing.

Playwright is a modern automation framework that allows developers and testers to interact with web applications programmatically. It supports multiple browsers and provides powerful features such as automatic waiting, reliable element handling, and built-in mechanisms to reduce flaky tests.

I created this repository while exploring ways to automate repetitive browser-based tasks and understand how automated testing frameworks work in real-world development environments. During security research and development workflows, many tasks involve interacting with web interfaces repeatedly. Learning tools like Playwright helps automate those interactions and makes testing more efficient.

This repository contains setup instructions, small experiments, and example scripts that demonstrate how Playwright can be used for browser automation, testing workflows, and interaction with modern web applications.

The goal of this project is to build a practical understanding of browser automation and to explore how automation tools can improve testing, debugging, and security research workflows.

## SETUP

for installation use  - ```pip install pytest-playwright```

to install required browser - ```playwright install```

for updating - ```pip install pytest-playwright playwright -U```

- playwright automatically wait for wide range of actionable checks to pass prioir to performing each action

- playwright are designed in a way that describes the expectation that need to be met


- the design choice all playwright to forget about flaky timeouts
