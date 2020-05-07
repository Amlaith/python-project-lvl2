from gendiff.generator import generate_diff

def test_answer():
    with open('./tests/fixtures/result.txt') as f:
        result = f.read().strip()

    assert generate_diff('./tests/fixtures/before.json', './tests/fixtures/after.json') == result
    assert generate_diff('./tests/fixtures/before.yml', './tests/fixtures/after.yml') == result
