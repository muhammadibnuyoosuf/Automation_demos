import pytest
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.sanity
def test_assert1():
    assert 5==4+1,"value mismatch"
    print("passed")
@pytest.mark.regression
@pytest.mark.sanity
def test_assert2():
    assert 5==4+1,"value mismatch"
    print("passed")
@pytest.mark.smoke
@pytest.mark.regression
def test_assert3():
    assert 5==4+1,"value mismatch"
    print("passed")
@pytest.mark.sanity
def test_assert4():
    assert 5==4+1,"value mismatch"
    print("passed")
@pytest.mark.smoke
def test_assert():
    assert 5==4+1,"value mismatch"
    print("passed")

