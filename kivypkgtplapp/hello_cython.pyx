# coding: utf8
"""
Example cython module.

http://docs.cython.org/src/tutorial/cython_tutorial.html
"""

def hello():
    return "Hello from Cython!"


cdef class Example(object):

    def __cinit__(self, dict stuff):
        self.uid = 1
        self.stuff = stuff

    cpdef hello(self, basestring key):
        return hello() + self.stuff[key]
