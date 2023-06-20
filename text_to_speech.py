import pyttsx3 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode

browser = webdriver.Chrome()

url = "https://platform.openai.com/docs/guides/gpt-best-practices"

# Load the page using Chrome driver
browser.get(url)

# Get the page source after it has been fully loaded
html = browser.page_source

# Create a BeautifulSoup object from the HTML content
soup = BeautifulSoup(html, "html.parser")

# initialize Text-to-speech engine  
engine = pyttsx3.init()  
# setting new voice rate (faster/slower)  
engine.setProperty("rate", 170)

# The Current index is here to help you move forward in the text
currentIndex = 43

lastText = ''
visible_text = [element.get_text(strip=True) for element in soup.find_all(text=True) if element.parent.name not in ["style", "script", "head", "title"]]

for p_tag in visible_text[currentIndex:]:
    text = p_tag
    if text == lastText:
        continue
    print('Current: ' + str(currentIndex) + ' ' + text)
    lastText = text
    engine.say(text)
    engine.runAndWait()
    currentIndex += 1

engine.stop()
