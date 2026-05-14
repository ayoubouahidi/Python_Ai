
import os
from mimetypes import guess_extension
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

DRIVER_PATH = ChromeDriverManager().install() 
