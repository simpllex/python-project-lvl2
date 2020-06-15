from gendiff.engine import return_string, read_file
import pytest


def test_build():
    old_json = read_file("./tests/fixtures/before.json")
    new_json = read_file("./tests/fixtures/after.json")
    result = open("./tests/fixtures/diff.txt", 'r').read()
    assert return_string(old_json, new_json) == result
    old_yml = read_file("./tests/fixtures/before.yml")
    new_yml = read_file("./tests/fixtures/after.yml")
    assert return_string(old_yml, new_yml) == result
    complex_result = open("./tests/fixtures/diff1.txt", 'r').read()
    complex_old = read_file("./tests/fixtures/before1.json")
    complex_new = read_file("./tests/fixtures/after1.json")
    assert return_string(complex_old, complex_new) == complex_result
def test_build_raises():
    """add() должно возникнуть исключение с неправильным типом param."""
    with pytest.raises(Exception) as excinfo:
        old = read_file("./tests/fixtures/before.xml")
        new = read_file("./tests/fixtures/after.xml")
        return_string(old, new)
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Invalid format, run --help!"