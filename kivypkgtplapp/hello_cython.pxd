
cdef class Example(object):
    cdef readonly int uid
    cdef dict stuff
    cpdef hello(self, basestring key)
