from queue import Queue
from threading import Thread

def do_work(q):
    while True:
        print(q.get(), end='\r')
        q.task_done()

q = Queue()
threads = 10

for thread in range(threads):
    worker = Thread(target=do_work, args=(q,))
    worker.daemon = True
    worker.start()

for y in range(10):
    for x in range(100):
        q.put(x + y * 100)
    q.join()
    print("Batch " + str(y) + " done.")