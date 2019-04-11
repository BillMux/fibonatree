# !/usr/bin/env python
# -*- coding: utf8 -*-

''' Contains methods and attributes of the Branch class '''
class Branch:
    ''' Creates branch '''
    def __init__(self, previous_branches=None, is_split=False):
        self.is_split = is_split
        self.growth = []

    def generate(self):
        if len(self.growth) > 0:
            self.growth[0].growth.extend([Branch(), Branch()])
        else:
            self.growth.append(Branch())
