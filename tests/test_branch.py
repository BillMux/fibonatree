# !/usr/bin/env python
# -*- coding: utf8 -*-

''' Branch class tests '''

from src.branch import Branch

def setup():
    ''' Setup tests '''
    global BRANCH
    BRANCH = Branch()

def test_starts_with_bool_split_attr():
    ''' Branch should be either split or not '''
    assert BRANCH.is_split is False
