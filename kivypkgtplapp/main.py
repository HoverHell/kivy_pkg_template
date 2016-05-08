#!/usr/bin/env python
# coding: utf8

from kivypkgtplapp import hello_cython
from kivypkgtplapp import sampleapp


def main():
    print("Main!")
    hello_cython.hello()
    app = sampleapp.SampleApp()
    app.run()


if __name__ == '__main__':
    main()
