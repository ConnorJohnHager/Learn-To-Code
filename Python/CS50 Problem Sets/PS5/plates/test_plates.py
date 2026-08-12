from plates import is_valid

# Remember to input 'python -m pip install -U pytest' in your terminal to be able to import
## Visit https://docs.pytest.org/en/stable/getting-started.html for more details

def test_is_valid_pass():
    assert is_valid("LUCAR10") == False
    assert is_valid("AA22AA") == False
    assert is_valid("MIN104") == True

    # Lucario and Minior are Pokemon names

def test_is_valid_fail(): # Purposely wrong
    assert is_valid("Y0SH1") == True # Should be false, can't have first number as 0 and can't have numbers in the middle
    assert is_valid("LUIGI") == False # Should be true, doesn't need to have numbers
    assert is_valid("MAR10") == False # Should be true, meets criteria