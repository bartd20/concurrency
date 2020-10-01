from datetime import datetime
from my_devices import devices
from my_functions import ssh_command2
from concurrent.futures import ProcessPoolExecutor,as_completed

# devices = cisco3, arista1, arista2, srx2

proc_list = []
max_procs = 4
proc_pool = ProcessPoolExecutor(max_procs)

start_t = datetime.now()
print("Start: " + str(start_t))

for elem in devices:
    proc = proc_pool.submit(ssh_command2, elem, "show version")
    proc_list.append(proc)

for elem in as_completed(proc_list):
    print(elem.result())

stop_t = datetime.now()

print("Stop : " + str(stop_t))
print("Run time: "+str(stop_t - start_t))
print("---------------")


