from datetime import datetime
from my_devices import devices
from my_functions import ssh_command2, ssh_command3
from concurrent.futures import ProcessPoolExecutor

# devices = cisco3, arista1, arista2, srx2

max_procs = 4

start_t = datetime.now()
print("Start: " + str(start_t))

with ProcessPoolExecutor(max_procs) as proc_pool:
    proc_out = proc_pool.map(ssh_command3, devices)

    for elem in proc_out:
        print(elem)

stop_t = datetime.now()

print("Stop : " + str(stop_t))
print("Run time: "+str(stop_t - start_t))
print("---------------")


