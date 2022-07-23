from datetime import datetime
from plyer import notification
alarm_time = input("Enter time in 'HH:MM:SS' format: ")
alarm_hour = alarm_time[0:2]
alarm_min = alarm_time[3:5]
alarm_sec = alarm_time[6:8]
print(f'your alarm will ring in {alarm_time}')
while True:
    time1 = datetime.now()
    current_hour = time1.strftime("%I")
    current_min = time1.strftime("%M")
    current_sec = time1.strftime("%S")
    if alarm_hour == current_hour :
        if alarm_min == current_min:
            if alarm_sec == current_sec:
                notification.notify(title='ahmed',message='wake up',timeout=10)  
                print('valid')
                break
