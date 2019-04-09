import pytest
from src.branch import Branch

def setup():
    global branch
    branch = Branch()

def test_starts_with_bool_split_attr():
    assert branch.is_split == False
