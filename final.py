from flask import Flask, render_template, Response, request, redirect, jsonify
import time
import StopwatchTracker as st
import threadtest as Clock
app = Flask(__name__)
app.debug = True
my_st = st.StopwatchTracker()
print(my_st)
watch = st.StopwatchTracker()


#timing=0
@app.route('/')
def index():
    #data = my_st.getTime()
    # return the results of clock()
    return render_template('home.html')

@app.route('/start_function')
def start_function():
    print("start")
    # start the stopwatch
    my_st.start()
    timer = my_st.getTime()
    while my_st.isRunning == True
        return render_template('home.html', 'timer': timer)
    # start the thread
    #watch = st.StopwatchTracker()
    #watch.start()
    #return render_template('home.html', timer=timer)
    
@app.route('/stop_function')
def stop_function():
    print("stop")
    my_st.stop()
    print(my_st.endTime)
    history = my_st.getHistory
    print(my_st.getHistory)
    return render_template('home.html', history=history)
    
    
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(use_reloader=False)
