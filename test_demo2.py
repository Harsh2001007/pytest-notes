import pytest

# creaitng tests

def test_matching():
    a = "hello"
    assert a == 'hi', "test fail as strings does not match."


def test_add():
    a = 2
    b= 2
    c = 4
    assert a+b == c , "Addition matched"

# creating a test as similar to new test in test_demo1.py

def test_similarSubtract():
    a = 10
    b = 10
    assert a-b == 1,"subtract failed in test_demo2.py"

# To run similar named test case use the command --> py.test -k similar -v -s


#---------------------------------------------------------- MARKS (TAGS) ----------------------------------------*

# used to run specific marked tests --> import pytest >>> just above the function write --> @pytest.mark.nameOfMark 

# creating tests with marks

@pytest.mark.i_am_a_mark
def test_markingTest2():
    print("i am in group1")

@pytest.mark.i_am_a_mark
def test_markSub():
    a = 10
    b = 10
    assert a-b == 1, 'subtraction success'

# To run marked test use the command --> py.test -m i_am_a_mark -v -s 

