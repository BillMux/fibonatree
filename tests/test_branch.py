# !/usr/bin/env python
# -*- coding: utf8 -*-

''' Branch class tests '''

from src.branch import Branch

def setup():
    ''' Setup tests '''
    global BRANCH
    BRANCH = Branch()

def test_init():
    ''' Branch refers to array of branches,
    should be either split or not '''
    assert BRANCH.is_split is False
    assert BRANCH.growth == []

def test_first_gen_has_one_single_branch():
    ''' First generation should grow one branch '''
    BRANCH.generate()
    assert len(BRANCH.growth) == 1
    assert isinstance(BRANCH.growth[0], Branch)
