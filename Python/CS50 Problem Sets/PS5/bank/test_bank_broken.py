from bank_broken import value

# Remember to input 'python -m pip install -U pytest' in your terminal to be able to import
## Visit https://docs.pytest.org/en/stable/getting-started.html for more details

def test_bank(): # Use to fix bank_broken.py
    assert value("Hello") == 0
    assert value("Hey there") == 20
    assert value("Good morning") == 100
