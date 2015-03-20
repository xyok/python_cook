#!/usr/bin/env python
#encoding:utf-8
'''进度条实现'''
import sys
import time
for x in xrange(0,51):
    sys.stdout.write("Computing: [%s%s] %i%%\r" % ('/' * x , '-' * (50 - x) , x *2))
    sys.stdout.flush()
    time.sleep(0.02)