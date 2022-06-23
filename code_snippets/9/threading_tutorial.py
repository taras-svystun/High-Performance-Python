import threading

print(threading.active_count(), threading.current_thread(),
threading.get_ident(), threading.get_native_id(), end='\n\n')

print(threading.enumerate(), threading.main_thread(), threading.TIMEOUT_MAX)

mydata = threading.local()
mydata.taras = 1
print(dir(mydata))