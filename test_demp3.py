import pytest

def test_fixTest(printer):
    print("I  will print after the fixture. ")
    

@pytest.fixture()
def printer():
    print("I am a fixture so i will run first")
    yield
    print("test is ok ok")
