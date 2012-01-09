#!/usr/bin/env python
import msgpackrpc

class AddHandler:
    def add(self, tid, x, y):
#        print tid, x, y
        return x + y

svr = msgpackrpc.Server(AddHandler())
address = msgpackrpc.Address('::', 18800)
svr.listen(address)
svr.start()


