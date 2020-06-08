from gendiff.engine import build_diff
import pytest


def test_build():
    assert build_diff("./tests/fixtures/before.json", "./tests/fixtures/after.json") == "{\nproxy : 123.234.53.22 verbose : True timeout : 50 timeout : 20 host : hexlet.io \n}"
    assert build_diff("./tests/fixtures/before.yml", "./tests/fixtures/after.yml") == "{\nproxy : 123.234.53.22 verbose : True timeout : 50 timeout : 20 host : hexlet.io \n}"

def test_build_raises():
    """add() должно возникнуть исключение с неправильным типом param."""
    with pytest.raises(Exception) as excinfo:
       build_diff("./tests/fixtures/before.xml", "./tests/fixtures/after.xml")
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Invalid format, run --help!"