import time
from plyer import notification

while True:
    time.sleep(3*60*60) # sleep for 3hrs
    notification.notify(
        title="Drink eater",
        message="stay hydrated",
        timeout=10
    )