import mysql.connector

class Database:

  # Log in to mySQL
  def __init__(self):
    self.mydb = mysql.connector.connect(
      host="localhost",
      user="iferrada",  #yourusername
      password="Vermillion#1" #yourpassword
    )
    self.mycursor = self.mydb.cursor()

    #Create the database if it does not exist
    self.mycursor.execute("CREATE DATABASE IF NOT EXISTS TimeStore")
    #Select Database
    self.mycursor.execute("USE TimeStore")
    #Create the table if it does not exist
    self.mycursor.execute("CREATE TABLE IF NOT EXISTS times (id INT AUTO_INCREMENT PRIMARY KEY, day int, hour int, min int, sec int)")


  #time input
  def storeData(self, day, hrs, min, sec):
    timeStore_day = day
    timeStore_hour = hrs
    timeStore_min = min
    timeStore_sec = sec
    self.mycursor.execute(f"INSERT INTO times (day, hour, min, sec) VALUES ('{timeStore_day}', {timeStore_hour}, '{timeStore_min}', '{timeStore_sec}')")

    self.mydb.commit()

  #return time columns
  def getHistory(self):
    self.mycursor.execute("SELECT * FROM times")

    myresult = self.mycursor.fetchall()

    return myresult