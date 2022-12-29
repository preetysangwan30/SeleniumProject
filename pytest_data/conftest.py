# Here is a fixture that is common for all and whereever mentioned in the fixture name in the TC
# in the working directory will be referred
# Other instances of the fixtures can be removed from all TCs and can only be called as the argument
import pytest

@pytest.fixture
def scope(): # Need not to have test_ coz its not a TC
    print("I will be executed first !!!") # will be executed before line 11
    yield # Code under this is invoked after whole execution of method which uses this fixture
    print("I'll be executing last !!!")