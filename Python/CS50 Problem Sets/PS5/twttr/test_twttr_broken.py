from twttr_broken import shorten

# Remember to input 'python -m pip install -U pytest' in your terminal to be able to import
## Visit https://docs.pytest.org/en/stable/getting-started.html for more details

def test_shorten(): # Use to fix twttr_broken.py
    assert shorten("Goodnight") == "Gdnght"
    assert shorten("Good morning") == "Gd mrnng" 
    assert shorten("Wild Animals: 501") == "Wld nmls: 501"