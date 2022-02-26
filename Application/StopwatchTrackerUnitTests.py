from tracemalloc import stop
import unittest
from unittest import mock
import time
from StopwatchTracker import StopwatchTracker

def convertTime(time):
    minutes = time // 60
    seconds = time % 60
    hours = minutes // 60
    minutes = minutes % 60
    days = hours // 24

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

if __name__ == '__main__':
    unittest.main()