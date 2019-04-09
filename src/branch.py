# !/usr/bin/env python
# -*- coding: utf8 -*-

''' Contains methods and attributes of the Branch class '''
class Branch:
    ''' Creates branch '''
    def __init__(self, is_split=False):
        self.is_split = is_split
        self.growth = []

    def generate(self):
        self.growth.append(self)
