# -------------------------------------------- PYTEST REQUISITES ---------------------------------------- 


# Any pytest file must start from test_ or end with _test
# Pytest method or function must start with test_.
# Any code must wrap in fucntion or method only.

import pytest


def test_greet():
    print("hello")

def test_bye():
    print("bye bye!")


# To run the above test open terminal/cmd >>> change current path to the pytest directory.
# command :  "py.test" --> run all the test ||  "py.test -v" --> run test cases with mentioned methods/functions || "py.test -v -s" run test cases with functions names + output of functions.


# creating tests on another file "test_demo2.py"

# Run only selected file test cases:-  "py.test filename.py -v -s"

# creating two test with a bit similar name in this file and file test demo2,py

def test_similarAdd():
    a = 10
    b = 10
    assert a +b == 20, "add is ok in demo1.py"

# To run similar named test case use the command --> py.test -k similar -v -s



#---------------------------------------------------------- MARKS (TAGS) ----------------------------------------*

# used to run specific marked tests --> import pytest >>> just above the function write --> @pytest.mark.nameOfMark 

# creating tests with same marks in this file as well as in test_demo2.py

@pytest.mark.i_am_a_mark
def test_markingTest():
    print("i am in group1")


@pytest.mark.i_am_a_mark
def test_markAdd():
    a = 10
    b = 10
    assert a+b == 20, 'add success'

# To run marked test use the command --> py.test -m i_am_a_mark -v -s 

# -------------------------------------------------FIXTURES-------------------------------------------*

# refer to test_demo3.py
# If any fixture is created and it it passed as a parameter in the tests then fixture condition  will be performed then test will be performed and later on yeild will be performed(if any yield data is responded).
# Fixture method can be of any name but it must have @pytest.fixture() applied over it.

# ---------------------------------------------- conftest file -------------------------------------*

# conftest.py is a file which is used to store fixtures only.
# It is used to define only fixtures and any sdet does not need to write fixtures in every file.
# Fixtures can be deifned in the file and sdet only needs to pass the fixtures to the test only

# creating a conftest.py file

# Instead to declaring fixture everytime for 'N' number of test cases , a SDET can define a class and pass the arguments accordingly.

# To run selectively test cases using fixtures --> use pattern 
# @pytest.mark.usefixtures("name of fixtures from conftest")
# class nameOfClass:
#   def testname(self):
#       conditions.