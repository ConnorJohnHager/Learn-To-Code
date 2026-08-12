from twttr import shorten

# Remember to input 'python -m pip install -U pytest' in your terminal to be able to import
## Visit https://docs.pytest.org/en/stable/getting-started.html for more details

def test_shorten_pass():
    assert shorten("Goodnight") == "Gdnght"
    assert shorten("Good morning") == "Gd mrnng"
    assert shorten("Wild Animals: 501") == "Wld nmls: 501"

def test_shorten_fail(): # Purposely wrong
    assert shorten("Goodnight") == "Gdnght " # Extra space
    assert shorten("Good morning") == "Gd mrng" # Missing 'n'
    assert shorten("Wild Animals: 501") == "Wld Anmls: 501" # 'A' should be removed