# !/usr/bin/env python
# -*- coding: utf8 -*-

''' Contains methods and attributes of the Tree class '''
class Tree:
    ''' Creates tree '''
    def __init__(self, branches=[1]):
        self.branches = branches

    def tick(self):
        '''Adds next num to the fib seq'''
        if len(self.branches) > 1:
            self.branches.append(self.branches[-1] + self.branches[-2])
        else: self.branches.append(1)
