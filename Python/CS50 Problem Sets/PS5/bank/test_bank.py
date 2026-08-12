from bank import value

# Remember to input 'python -m pip install -U pytest' in your terminal to be able to import
## Visit https://docs.pytest.org/en/stable/getting-started.html for more details

def test_bank_pass():
    assert value("Hello") == 0
    assert value("Hey there") == 20
    assert value("Good morning") == 100

def test_bank_fail(): # Purposely wrong
    assert value("Hiya") == 0 # Should be 20
    assert value("Hello, good morning") == 100 # Should be 0
    assert value("Goodbye") == 0 # Should be 100 even though it's a farewell
