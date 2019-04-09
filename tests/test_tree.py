from src.tree import Tree

def setup():
    ''' Setup tests '''
    global tree
    tree = Tree()

def test_start_seq_from_one():
    ''' Branches array starts with a number one '''
    assert tree.branches == [1]

def test_first_tick_adds_one():
    ''' First time "tick" is called, adds one '''
    tree.tick()
    assert tree.branches == [1, 1]

def test_following_ticks_add_fib_nums():
    ''' Following time "tick" is called, adds sum of previous two nums '''
    for _ in range(5): tree.tick()
    assert tree.branches == [1, 1, 2, 3, 5, 8, 13]
