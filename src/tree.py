# !/usr/bin/env python
# -*- coding: utf8 -*-

''' Contains methods and attributes of the Tree class '''
class Tree:
    ''' Creates tree '''
    def __init__(self, fib=[1]):
        self.fib = fib

    def tick(self):
        '''Adds next num to the fib seq'''
        if len(self.fib) > 1:
            self.fib.append(self.fib[-1] + self.fib[-2])
        else: self.fib.append(1)
