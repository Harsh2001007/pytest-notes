import pytest

# ------------------This is a regular test (which will execute after fixture but before fixture's yield --------------------------------
def test_fixTest(printer):
    print("I  will print after the fixture. ")


# -------------- This is a fixture which will always run before applied tests but the yield will always get printed in the end of that specific test --------------------------------------
@pytest.fixture()
def printer():
    print("I am a fixture so i will run first")
    yield
    print("test is ok ok")
