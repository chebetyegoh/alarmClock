from datetime import datetime as dt
from playsound import playsound
import gi
# function to validate the time input by the user


def validate_time(alarm_time):
    if len(alarm_time) != 11:
        return 'Invalid format! please try again...'
    elif int(alarm_time[0:2]) > 12:
        return 'Invalid HOUR! please try again...'
    elif int(alarm_time[3:5]) > 59:
        return 'Invalid MINUTE! please try again...'
    elif int(alarm_time[6:8]) > 59:
        return 'Invalid SECOND! please try again...'
    else:
        return 'OK'


alarm_time = input("Enter time in 'HH:MM:SS AM/PM' format:")

validate = validate_time(alarm_time.lower())
if validate != 'ok':
    print(validate)
else:
    print(f"Setting alarm for time: {alarm_time}")


# separately store  the values of alarm time into different variables

alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_second = alarm_time[6:8]
alarm_period = alarm_time[9:].upper()

print(f'Waiting for alarm {alarm_time}')
while True:
    now = dt.now()
    current_hour = now.strftime("%I")
    current_min = now.strftime("%M")
    current_second = now.strftime("%S")
    current_period = now.strftime("%p")

    if alarm_period == current_period:
        if alarm_second == current_second:
            if alarm_minute == current_min:
                if alarm_hour == current_hour:
                    print("Wake up Sugar!")
                    #playsound('/home/chebet/dev/alarm-clock/nana_fofie_j_en_vaux_la_peine_official_video_mp3_75312.mp3')
                    print('\a')
                    break
