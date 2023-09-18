from wdSettings import *
from datetime import date

#date input
choosenDate = input("Enter date in format: DD/MM/YYYY: ")



websiteURL = "https://www.whoscored.com/LiveScores"
driver.get(websiteURL)

# window close
acceptWindow = driver.find_element(by="xpath", value=("//*[text()='AGREE']"));
acceptWindow.click()

# date choosing window according to input value
dateWindow = driver.find_element(by="id", value="toggleCalendar")
dateWindow.click()


