import pytest


@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True
#https://docs.pytest.org/en/latest/reference/reference.html#pytest.mark.xfail

@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False
