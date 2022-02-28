from flask import Flask,render_template,Response, request, redirect
import time
import StopwatchTracker as st
app = Flask(__name__)
app.debug = True
my_st = st.StopwatchTracker()
print(my_st)

@app.route('/')
def index():
    data = my_st.getTime()
    return render_template('home.html', data=data)

@app.route('/start_function')
def start_function():
    print("start")
    my_st.start()
    #if request.method =='POST':
        #timer_result = request.form[my_st.getTime]
    #timer_result = "hello"
    return ("nothing")
    #my_st = st.StopwatchTracker()
    
    
@app.route('/stop_function')
def stop_function():
    print("stop")
    my_st.stop()
    print(my_st.endTime)
    return("nothing")
    
    
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()
