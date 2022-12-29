# Here we will discuss fixtures, fixtures are nothing but the preresquisites
# or programs that run post execution

import pytest

@pytest.fixture
def scope(): # Need not to have test_ coz its not a TC
    print("I will be executed first !!!") # will be executed before line 11
    yield # Code under this is invoked after whole execution of method which uses this fixture
    print("I'll be executing last !!!")

def test_fixtureDemo(scope):
    print("I'll be executed second !!!") 
