import pytest

# @pytest.fixture()
# def before_after():
#     print("before")
#     yield
#     print("\nafter")
def test_first():
    assert 1==1

def test_first2(before_after):
    assert 2==2