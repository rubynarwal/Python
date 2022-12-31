import time
time = time.strftime('%H')
if int(time)>=19:
    print("Good evening \n")
elif int(time)<13:
    print("Good morning \n")
elif int(time)>=12:
    print("Good afternoon \n")
elif int(time)==27:
    print("The new day has started!")