# The test file must start with test_
# All of the code must be written inside the methods 
# The method name should begin with test_ 
# Tests can be marked (tagged) as @pytest.mark.Smoke (Smoke is mark) and run with -m 

import pytest

def test_firstcode():
    print("first pytest code")

@pytest.mark.Smoke # Smoke is like a category
def test_greet():
    print("Good Morning!!!")