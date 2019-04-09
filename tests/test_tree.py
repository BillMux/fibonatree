# !/usr/bin/env python
# -*- coding: utf8 -*-

''' Tree class tests '''

from src.tree import Tree

def setup():
    ''' Setup tests '''
    global TREE
    TREE = Tree()

def test_start_seq_from_one():
    ''' Branches array starts with a number one '''
    assert TREE.fib == [1]

def test_first_tick_adds_one():
    ''' First time "tick" is called, adds one '''
    TREE.tick()
    assert TREE.fib == [1, 1]

def test_following_ticks_add_fib_nums():
    ''' Following time "tick" is called, adds sum of previous two nums '''
    for _ in range(5):
        TREE.tick()
    assert TREE.fib == [1, 1, 2, 3, 5, 8]
