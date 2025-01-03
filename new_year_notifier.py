import time
from datetime import datetime
from plyer import notification

while True:
    today=datetime.today()  #today=take today date and time from the module
    
    if today.month==1 and today.day==1: #check if today is month 1 and day is day 1
        notification.notify(
            title="Happy new year",
            message="wishing u a Happy new year",
            timeout=10
        )
        
        time.sleep(86400) #sleep for 24 hrs