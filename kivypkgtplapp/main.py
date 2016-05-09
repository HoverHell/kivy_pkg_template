#!/usr/bin/env python
# coding: utf8


def main():
    print("Main!")
    # Things are imported here rather than on the top level to track
    # errors.

    # Cython
    from kivypkgtplapp import hello_cython
    print(hello_cython.hello())
    print(hello_cython.Example({'a': " (cls)"}).hello('a'))

    # Cython that imports cython
    from kivypkgtplapp import hello_cython_cython
    # hello_cython_cython.hello()
    hello_cython_cython.Subexample({'a': " (cls)"}).hello('a')

    # print("import kivy")
    # import kivy
    # print("import kivy.properties")
    # import kivy.properties
    # print("import kivy._event")
    # import kivy._event
    # print("kivy._event", repr(kivy._event.ObjectWithUid()))
    # import kivy.event
    # print("kivy.event", repr(kivy.event.ObjectWithUid()))

    from kivypkgtplapp import sampleapp
    app = sampleapp.SampleApp()
    app.run()


if __name__ == '__main__':
    main()
