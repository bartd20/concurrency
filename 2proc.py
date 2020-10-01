from datetime import datetime
from my_devices import devices
from my_functions import ssh_command
from multiprocessing import Process

procs = []

start_t = datetime.now()

for elem in devices:
    my_proc = Process(target=ssh_command, args=(elem,"show version"))
    my_proc.start()
    procs.append(my_proc)

for some_proc in procs:
    some_proc.join()    

stop_t = datetime.now()

print("Run time: "+str(stop_t - start_t))

