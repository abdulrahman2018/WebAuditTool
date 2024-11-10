# Web Audit Tool 🕵️‍♂️

## Overview

This project is a **web audit tool** built using Python, **BeautifulSoup**, **Selenium**, and **Axe-core**. It performs automated checks on websites for critical factors such as SSL certificates, SEO compliance (noindex tag), favicon presence, page load time, cookie banners, and accessibility violations. The goal is to ensure that websites meet basic web standards and provide a better user experience.

## Features

The tool performs the following checks:

1. **SSL Certificate (HTTPS Check)**  
   Verifies whether the website has an SSL certificate and uses HTTPS.

2. **Noindex Tag**  
   Checks if the website includes a `noindex` meta tag, which tells search engines not to index the page.

3. **Favicon Presence**  
   Detects if the website has a favicon (`<link rel="icon">` tag).

4. **Page Load Time**  
   Measures the page load time using Selenium WebDriver to simulate real user behavior and wait for the page to load completely.

5. **Cookie Banner Detection**  
   Identifies whether a website has a cookie banner, ensuring compliance with privacy regulations (e.g., GDPR).

6. **Accessibility Compliance**  
   Uses **Axe-core** to run accessibility checks on the page, ensuring compliance with **WCAG 2.1** standards for color contrast, image alt text, form labels, and more.

## Installation

### Prerequisites

- Python 3.x
- `pip` for managing Python packages
- **Selenium**: A Python package to automate web browser interactions.
- **Axe Selenium Python**: A wrapper to use Axe-core with Selenium for accessibility testing.
- **ChromeDriver**: Make sure you have **ChromeDriver** installed and configured for Selenium.

### Steps to Install

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/abdulrahman2018/WebAuditTool.git
    ```

2. Navigate to the project directory:

    ```bash
    cd WebAuditTool
    ```

3. Install the necessary Python libraries:

    ```bash
    pip install -r requirements.txt
    ```

4. Download and set up **ChromeDriver** (ensure it's compatible with your Chrome version).

### Requirements

To run the audit tool, you'll need the following Python libraries:

- `requests`: For making HTTP requests and checking the SSL certificate.
- `beautifulsoup4`: For parsing and extracting HTML content.
- `selenium`: For simulating user interactions and checking dynamic content.
- `axe-selenium-python`: For accessibility testing.

You can install these dependencies using:

```bash
pip install requests beautifulsoup4 selenium axe-selenium-python
