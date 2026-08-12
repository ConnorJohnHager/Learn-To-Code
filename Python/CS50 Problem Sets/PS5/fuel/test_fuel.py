from fuel import convert, gauge

# Remember to input 'python -m pip install -U pytest' in your terminal to be able to import
## Visit https://docs.pytest.org/en/stable/getting-started.html for more details

def test_convert_pass():
    assert convert("3/4") == 75
    assert convert("-5/6") == ValueError
    assert convert("1/0") == ZeroDivisionError

def test_convert_fail(): # Purposely wrong
    assert convert("2/3") == 66.6 # Should be 66
    assert convert("0/1") == ZeroDivisionError # Should be 0

def test_gauge_pass():
    assert gauge(101) == ValueError
    assert gauge(50) == "50%"
    assert gauge(1) == "E"

def test_gauge_fail(): # Purposely wrong
    assert gauge(99) == "99%" # Should be 'F'
    assert gauge(0) == ValueError # Should be 'E'