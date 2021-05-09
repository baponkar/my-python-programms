import time
import threading 


def func(val):
    print("Sleeping {}".format(val))
    time.sleep(val)
    print("Done!")


in_time = time.perf_counter()

#creating two threds
t1 = threading.Thread(target=func, args=[1])
t2 = threading.Thread(target=func, args=[1])

#Starting two thread
t1.start()
t2.start()


#waiting main thread to complete the child thread
t1.join()
t2.join()


fin_time = time.perf_counter()



print("This code take {} second(s) to complete".format(round(fin_time - in_time), 2))
