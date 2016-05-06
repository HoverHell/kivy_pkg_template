#!/usr/bin/env python
# coding: utf8


def main():
    print("Main!")
    from kivypkgtplapp import hello_cython
    hello_cython.hello()
    from kivypkgtplapp import sampleapp
    app = sampleapp.SampleApp()
    app.run()


if __name__ == '__main__':
    main()
