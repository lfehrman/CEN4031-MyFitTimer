#imports
import time
from DataAccess.DataTable import Database

class StopwatchTracker:

    #Initialize variables
    def __init__(self):
        self.isRunning = False
        self.database = Database()
        self.startTime = int(time.time()//1)
        self.endTime = int(time.time()//1)

    #start method
    #if the timer is running will return
    #otherwise will set the timer to running and set the start time to current
    def start(self):
        if(self.isRunning):
            return

        self.isRunning = True
        self.startTime = int(time.time()//1)

    #stop method
    #returns if the timer is not running
    #otherwise will stop the timer, set the end time, and record the elapsed time to the database
    def stop(self):
        if(not(self.isRunning)):
            return

        self.isRunning = False
        self.endTime = int(time.time()//1)

        #Gets time and splits it to be sent to database
        timeParts = self.getTime().split(":")

        #Sends the time to the database for storage as (days, hours, minutes, seconds)
        self.database.storeData(timeParts[0], timeParts[1], timeParts[2], timeParts[3])

    #getTime method
    #if the timer is running, will return the time elapsed from start to current
    #if timer is stopped, will return time between start and end
    #Return string format = "days:hours:minutes:seconds"
    def getTime(self):
        if(self.isRunning):
            self.endTime = int(time.time()//1)
        
        elapsed = self.endTime - self.startTime

        minutes = elapsed // 60
        seconds = elapsed % 60
        hours = minutes // 60
        minutes = minutes % 60
        days = hours // 24

        return f"{days}:{hours}:{minutes}:{seconds}"

    #TODO
    #getHistory method
    #returns an array of all values from the database
    def getHistory(self):
        history = self.database.getHistory()
        formatedHistory = []
        for times in history:
            formatedHistory.append(f"{times[1]}:{times[2]}:{times[3]}:{times[4]}")
        return formatedHistory
        



            
