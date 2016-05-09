# coding: utf8
"""
Example cython module that loads another cython module. For testing
the builds.
"""

def hello():
    import kivypkgtplapp.hello_cython as internal
    print(internal.hello() + ' (wrap)')


cdef class Subexample(Example):
    cpdef hello(self, basestring key):
        print(Example.hello(self, key) + ' (subcls)')
