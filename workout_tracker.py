import mysql.connector
from mysql.connector import Error

mydb = mysql.connector.connect(
  host="<hostname>",
  user="<admin_user>",
  passwd="<password_db>",
  database = "<database_identity>"
)
workouts = []

def uno():
    workout = input('What kind of workout?  ')
    x,y = "bike","run"
    if workout == x.upper() or y.upper():
        workouts.append(workout)
    else:
        print('Need to input either BIKE or RUN')
    #print(f'Congrats on working out! Lets keep going!')

def dose():
    x = 1
    while x != 0:
        try:
            duration = float(input('How long was your workout? '))
            workouts.append(duration)
            x = x -1
        except ValueError:
            print('Needs to be a float-- Ex: 54.23')

def tres():
    print('-------')
    print("""For Day use: Mon,Tue,Wend,Thur,Fri,Sat,Sun
             For Date use: Format DD-MM-YY
             For Feelings use: Input as many as needed""")
    day = input('What day did you workout? ')
    workouts.append(day)
    date = input('What is todays date? ')
    workouts.append(date)
    feeling = input('How did you feel after todays workout? ')
    workouts.append(feeling)

def cuatro():
    typeof = input('Did you workout intense or light today?')
    if typeof.lower() == "intense":
        workouts.append("Intense")
    elif typeof.lower() == "light":
        workouts.append("Light")
    ask = input('Did you do workout 100? (Y) OR (N) ')
    if ask.upper() == "Y":
        for num in range(4):
            workouts.append(100)
        for i in range(2):
            workouts.append(15)
    elif ask.upper() == "N":
        for nums in range(4):
            workouts.append(0)
        for nums in range(2):
                workouts.append(0)
    rope = input("Did you jump rope?")
    if rope.upper() == "Y":
        workouts.append("Yes")
    else:
        workouts.append("No")


def cinco():
    uno()
    dose()
    tres()
    cuatro()
cinco()
print(workouts)


sql = ( """INSERT INTO 
                lifts(WorkoutType, Duration, Day, Date, Feeling, Level, Pushups, Pullups, Squats, Situps, OverheadPress, BentOverRow, JumpRope) 
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """ ) 
mycursor =  mydb.cursor()

mycursor.execute(sql, workouts)
mydb.commit()
