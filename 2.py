from datetime import datetime
from my_devices import devices
from my_functions import ssh_command
import threading

start_t = datetime.now()

for elem in devices:
    my_thread = threading.Thread(target=ssh_command, args=(elem,"show version"))
    my_thread.start()

main_thread = threading.currentThread()
for some_thread in threading.enumerate():
    if some_thread != main_thread:
        print(some_thread)
        some_thread.join()    

stop_t = datetime.now()

print("Run time: "+str(stop_t - start_t))

