from flask import Flask, render_template, request, redirect, url_for
import time
# st shorthand for StopwatchTracker.py
import StopwatchTracker as st
app = Flask(__name__)
app.debug = True
# StopwatchTracker constructor
my_st = st.StopwatchTracker()
#fake_database = ['00:00:00:03', '00:00:01:05']

# Home Page home.html
@app.route('/')
def index():
    return render_template('home.html')

# When start button is clicked run the start(self) timer    
@app.route('/start_function')
def start_function():
    # Show that the stopwatch started in the console
    print("start")
    # start the stopwatch
    my_st.start()
    return ("nothing") 

# When the stop button is clicked open a new tab
@app.route('/success/<timer>')
def success(timer):
   # Display Elapsed time
   return 'Elapsed Time: %s' % timer 

# When the stop button is clicked Post the user input to this route  
@app.route('/stopwatch',methods = ['POST', 'GET'])
def stopwatch():
    # Show that the stopwatch stopped in the console
    print("stop")
    # Stop the stopwatch
    my_st.stop()
    # Show that an end time was created in the console
    print(my_st.endTime)
    # Store the times
    my_st.getTime()
    # Calculate the elapsed time
    elapsedTime = my_st.endTime - my_st.startTime
    # Calculate the days, hours, minutes, and seconds
    minutes = elapsedTime // 60
    seconds = elapsedTime % 60
    hours = minutes // 60
    minutes = minutes % 60
    days = hours // 24
    # Format the time
    formattedTime = f"{days:02d}:{hours:02d}:{minutes:02d}:{seconds:02d}"
    if request.method == 'POST':
        # Change the POST to the formatted time
        user = formattedTime
        # Return the user variable as timer
        return redirect(url_for('success',timer = user))

@app.route('/history/<times>')
def history(times):
    return 'History of Elapsed Times: %s' % times

@app.route('/stored',methods = ['POST', 'GET'])
def stored():
    # Show that the times were stored in the console
    print("stored")
    # Receive an array of all values form the database
    timerHistory = my_st.getHistory()
    #timerHistory = fake_database
    if request.method == 'POST':
        # Change the user input to the getHistory method
        data = timerHistory
        # return the data
        return redirect(url_for('history',times = data))
   
# About Page about.html    
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()
