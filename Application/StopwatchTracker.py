#imports
import time

class StopwatchTracker:

    #Initialize variables
    def __init__(self):
        self.isRunning = False
        self.database = None
        self.startTime = time.time()
        self.endTime = time.time()

    #start method
    #if the timer is running will return
    #otherwise will set the timer to running and set the start time to current
    def start(self):
        if(self.isRunning):
            return

        self.isRunning = True
        self.startTime = time.time()

    #stop method
    #returns if the timer is not running
    #otherwise will stop the timer, set the end time, and record the elapsed time to the database
    def stop(self):
        if(not(self.isRunning)):
            return

        self.isRunning = False
        self.endTime = time.time()

        self.database.storeTime(self.getTime())

    #getTime method
    #if the timer is running, will return the time elapsed from start to current
    #if timer is stopped, will return time between start and end
    #Return string format = "days:hours:minutes:seconds"
    def getTime(self):
        if(self.isRunning):
            self.endTime = time.time()
        
        elapsed = self.endTime - self.startTime

        minutes = elapsed // 60
        seconds = elapsed % 60
        hours = minutes // 60
        minutes = minutes % 60
        days = hours // 24

        return f"{days}:{hours}:{minutes}:{seconds}"



            
