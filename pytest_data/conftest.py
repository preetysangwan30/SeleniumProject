# Here is a fixture that is common for all and whereever mentioned in the fixture name in the TC
# in the working directory will be referred
# Other instances of the fixtures can be removed from all TCs and can only be called as the argument
import pytest

@pytest.fixture(scope="class") # Adding the scope to the class level, hence it is independent of the nos of methods in the class

def scope(): # Need not to have test_ coz its not a TC
    print("I will be executed first !!!") # will be executed before line 11
    yield # Code under this is invoked after whole execution of method which uses this fixture
    print("I'll be executing last !!!")


#Creating another fixture which also has to send out data to the method it is called from

@pytest.fixture()
def dataLoad():
    print("We'll be sending out data to whoever asked for it")
    return ["Divya", "Pateriya", "Divyapateriya"] # Include data in the list