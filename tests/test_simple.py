from gendiff.engine import build_diff


def test_build():
    assert build_diff("./tests/fixtures/before.json", "./tests/fixtures/after.json") == "{\nproxy : 123.234.53.22 verbose : True timeout : 50 timeout : 20 host : hexlet.io \n}"