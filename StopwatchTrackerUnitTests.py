from tracemalloc import stop
import unittest
import time
from DataAccess.DataTable import Database
from Application.StopwatchTracker import StopwatchTracker

def convertTime(time):
    minutes = int(time // 60)
    seconds = int(time % 60)
    hours = int(minutes // 60)
    minutes = int(minutes % 60)
    days = int(hours // 24)

    return f"{days}:{hours}:{minutes}:{seconds}"

class StopwatchTrackerUnitTests(unittest.TestCase):

    def test_start(self):
        stopwatch = StopwatchTracker()
        stopwatch.start()
        startTime = time.time() // 1
        self.assertEqual(stopwatch.isRunning, True)
        self.assertEqual(stopwatch.startTime//1, startTime)
        time.sleep(2)
        stopwatch.start()
        self.assertEqual(stopwatch.isRunning, True)
        self.assertEqual(stopwatch.startTime//1, startTime)
        
    def test_stop(self):
        stopwatch = StopwatchTracker()
        stopwatch.start()
        stopwatch.stop()
        endTime = time.time()//1
        self.assertEqual(stopwatch.isRunning, False)
        self.assertEqual(stopwatch.endTime//1, endTime)
        time.sleep(2)
        stopwatch.stop()
        self.assertEqual(stopwatch.isRunning, False)
        self.assertEqual(stopwatch.endTime//1, endTime)

    def test_getTime(self):
        stopwatch = StopwatchTracker()
        stopwatch.start()
        time.sleep(2)
        self.assertEqual(stopwatch.getTime(), convertTime(time.time() - stopwatch.startTime))
        time.sleep(2)
        self.assertEqual(stopwatch.getTime(), convertTime(time.time() - stopwatch.startTime))
        stopwatch.stop()
        elapsedTime = convertTime(time.time() - stopwatch.startTime)
        self.assertEqual(stopwatch.getTime(), elapsedTime)
        time.sleep(2)
        self.assertEqual(stopwatch.getTime(), elapsedTime)

    def test_getHistory(self):
        stopwatch = StopwatchTracker()
        database = Database()
        swHistory = stopwatch.getHistory()[0]
        dbHistory = database.getHistory()[0]
        dbHistory = f"{dbHistory[1]}:{dbHistory[2]}:{dbHistory[3]}:{dbHistory[4]}"
        self.assertEqual(swHistory, dbHistory)

if __name__ == '__main__':
    unittest.main()