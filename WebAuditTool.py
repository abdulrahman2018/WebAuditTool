import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from axe_selenium_python import Axe
import time

# Define your URL
url = "https://www.amazon.com"  # Real website link for testing

# 1. Check if the website has an SSL certificate (HTTPS)
def check_ssl_certificate(url):
    response = requests.get(url)
    if response.url.startswith("https://"):
        print("The website has an SSL certificate (HTTPS).")
    else:
        print("The website does not have an SSL certificate (HTTPS).")

# 2. Check if a noindex tag is present
def check_noindex_tag(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    noindex_tag = soup.find('meta', {'name': 'robots', 'content': 'noindex'})
    if noindex_tag:
        print("The website has a noindex tag.")
    else:
        print("The website does not have a noindex tag.")

# 3. Check for favicon (handling multiple link types)
def check_favicon(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    favicon_tag = soup.find('link', rel=lambda x: x and 'icon' in x.lower())
    if favicon_tag:
        print("The website has a favicon.")
    else:
        print("The website does not have a favicon.")

# 4. Check for page load time using Selenium (simulate real browser behavior)
def check_page_speed(url):
    driver = webdriver.Chrome()  # Make sure you have ChromeDriver installed
    driver.get(url)
    start_time = time.time()
    
    # Wait for the page to load completely using WebDriverWait for accuracy
    driver.implicitly_wait(10)  # Wait for up to 10 seconds
    load_time = time.time() - start_time
    print(f"Page load time: {load_time:.2f} seconds")
    
    driver.quit()

# 5. Check for missing cookie banner using Selenium
def check_cookie_banner(url):
    driver = webdriver.Chrome()  # Make sure you have ChromeDriver installed
    driver.get(url)
    
    # Look for a cookie banner (you may need to adjust the XPath or search term depending on the site)
    cookie_banner = driver.find_elements(By.XPATH, "//*[contains(text(), 'cookie')]")
    if cookie_banner:
        print("The website has a cookie banner.")
    else:
        print("The website does not have a cookie banner.")
    
    driver.quit()

# 6. Check for accessibility (barrier-free website) using Axe and Selenium
def check_accessibility(url):
    driver = webdriver.Chrome()
    driver.get(url)
    
    axe = Axe(driver)
    axe.inject()  # Inject axe-core into the page
    
    # Run the accessibility tests
    results = axe.run()
    violations = results['violations']
    if violations:
        print(f"Accessibility violations found: {len(violations)}")
        for violation in violations:
            print(f"Description: {violation['description']}")
            for node in violation['nodes']:
                print(f"  - {node['html']}")
    else:
        print("No accessibility violations found.")
    
    driver.quit()

# Run all checks
def run_checks(url):
    check_ssl_certificate(url)
    check_noindex_tag(url)
    check_favicon(url)
    check_page_speed(url)
    check_cookie_banner(url)
    check_accessibility(url)

# Execute the checks
run_checks(url)
