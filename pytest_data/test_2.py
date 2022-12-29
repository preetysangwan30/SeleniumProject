import pytest

@pytest.mark.Smoke
@pytest.mark.skip
def test_AssertCheck():
	msg = "Hello"
	assert msg == "Hi" , "Strings do not match" # Message when there is an assertion error


@pytest.mark.xfail
def test_excerpt():
	print("An example for xfail")
