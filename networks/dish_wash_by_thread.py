import threading,queue
import time



"""
First wash dish then dry
"""

def washer(dishes, dish_queue):
    for dish in dishes:
        print("Washing {}".format(dish))
        time.sleep(1)
        dish_queue.put(dish)


def dryer(dish_queue):
    while True:
        dish = dish_queue.get()
        print("Drying " ,dish)
        time.sleep(2)
        dish_queue.task_done()


dish_queue = queue.Queue()
for n in range(2):
    dryer_thread = threading.Thread(target=dryer, args=(dish_queue,))
    dryer_thread.start()

dishes = [ 'salad', 'bread', 'entree', 'desert' ]
washer(dishes, dish_queue)
dish_queue.join()
