from datetime import datetime
from my_devices import devices
from my_functions import ssh_command2
from concurrent.futures import ThreadPoolExecutor,as_completed

# devices = cisco3, arista1, arista2, srx2

thread_list = []
max_threads = 4
thread_pool = ThreadPoolExecutor(max_threads)

start_t = datetime.now()
print("Start: " + str(start_t))

for elem in devices:
    thread = thread_pool.submit(ssh_command2, elem, "show version")
    thread_list.append(thread)

for elem in as_completed(thread_list):
    print(elem.result())

stop_t = datetime.now()

print("Stop : " + str(stop_t))
print("Run time: "+str(stop_t - start_t))
print("---------------")


