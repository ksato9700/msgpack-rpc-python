#!/usr/bin/env python
import sys
import random
import threading

import msgpackrpc

address = msgpackrpc.Address('::1', 18800)

class DummyLock:
    def acquire(self):
        pass

    def release(self):
        pass

#lock = DummyLock()
lock = threading.Lock()

def send_request(tid, address):
    client = msgpackrpc.Client(address)
    a = random.randint(-sys.maxint/2, sys.maxint/2)
    b = random.randint(-sys.maxint/2, sys.maxint/2)
    try:
        lock.acquire()
        ftr = client.call_async('add', tid, a, b)
        result = ftr.get()
        lock.release()
        assert result == a+b
        print threading.current_thread().ident, "done"
    except AssertionError as e:
        print result, a+b
    except Exception as e:
        print e
        raise

N = 100
threads = []
for tid in range(N):
    t = threading.Thread(target=send_request, args=(tid, address))
    threads.append(t)
    t.start()

[t.join(5) for t in threads]    




