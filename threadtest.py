import threading
import StopwatchTracker as st
import time

def clock(watch):
    # call getTime every half second
    currentTime = time.time()
    lastTime = time.time()
    while 1:
        currentTime = time.time()
        if currentTime >= lastTime + .5:
            result = watch.getTime()
            print(result)
            # TODO
            # send result to HTML
            lastTime = time.time()

# debug
'''
watch = st.StopwatchTracker()
watch.start()
x = threading.Thread(target=clock,args=(watch,))
x.start()
time.sleep(2)
#y_watch = st.StopwatchTracker()
#y_watch.start()
#y = threading.Thread(target=clock,args=(y_watch,))
#y.start()
'''
