from wdSettings import *
import datetime

# date input - return as INT numbers
enteredDate = input("Enter date in format: DD-MM-YYYY: ")


year, month, day = map(int, enteredDate.split('-'))
choosenDate = datetime.datetime(day, month, year)
matchDay = choosenDate.day
matchMonth = choosenDate.month
matchYear = choosenDate.year

print("test git")



# websiteURL = "https://www.whoscored.com/LiveScores"
# driver.get(websiteURL)
#
# # window close
# acceptWindow = driver.find_element(by="xpath", value=("//*[text()='AGREE']"));
# acceptWindow.click()
#
# # date choosing window according to input value
# dateWindow = driver.find_element(by="id", value="toggleCalendar")
# dateWindow.click()
