import pytest

@pytest.fixture()
def conf_demo():
    print("i am a fixture in conftest and i am applied on test_demo4.py and test_demo5.py")


# --- creating a fixture which will use in define class in test_demo6.py -----------------*

@pytest.fixture()
def conf_classFixture():
    print("I am applied to a class")
    yield
    print("i am a last one")

# creating a fixture

@pytest.fixture()
def dataProvider():
    print("this is data provider")
    a = 5
    b = 5
    return(a+b) #this is the final data

