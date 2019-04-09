from src.branch import Branch

def setup():
    ''' Setup tests '''
    global branch
    branch = Branch()

def test_starts_with_bool_split_attr():
    ''' Branch should be either split or not '''
    assert branch.is_split is False
