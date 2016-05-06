# coding: utf8
"""
Small sample Kivy app.

https://kivy.org/docs/tutorials/pong.html
"""
from kivy.app import App
from kivy.uix.widget import Widget


class Sample(Widget):
    pass


class SampleApp(App):

    def build(self):
        root = Sample()
        return root
