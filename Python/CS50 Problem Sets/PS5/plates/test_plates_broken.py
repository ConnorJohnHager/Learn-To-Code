from plates_broken import is_valid

# Remember to input 'python -m pip install -U pytest' in your terminal to be able to import
## Visit https://docs.pytest.org/en/stable/getting-started.html for more details

def test_is_valid(): # Use to fix plates_broken.py
    assert is_valid("LUCAR10") == False
    assert is_valid("MAR10") == True
    assert is_valid("Y0SH1") == False