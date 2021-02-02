from selenium import webdriver #Import the webdriver to launch Chrome driver here
from selenium.webdriver.chrome.options import Options #Import Options from Selenium to configure our driver
from githubConnexion import githubConnect

options = Options() #Declare options
options.headless = True #True=the driver won't be launch and False it will be launch
options.add_argument("--window-size=1920,1080") #Size of driver's window
options.add_argument("--incognito") #If you add this argument, the driver will launch a private session
DRIVER_PATH = "your_driver_path" #Replace by the path of your driver's executable
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH) #Create and init with options your driver

githubConnect(driver, "your_github_username", "your_github_password", True)

driver.quit() #Close the driver at the end of the program