import pytest
from src.tree import Tree

def setup():
    global tree
    tree = Tree()

def test_start_seq_from_one():
    assert tree.branches == [1]

def test_first_tick_adds_one():
    tree.tick()
    assert tree.branches == [1, 1]

def test_following_ticks_add_fib_nums():
    for i in range(5): tree.tick()
    assert tree.branches == [1, 1, 2, 3, 5, 8, 13]
