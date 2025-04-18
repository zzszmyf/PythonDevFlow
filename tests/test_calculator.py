from src.calculator import add
# Write your test functions here
def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0