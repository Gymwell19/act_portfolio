import sys
import os
# Ensure 'app' is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
from app.infix_postfix import infix_to_postfix

def test_pages():
    client = app.test_client()
    # Added /programming/infix and /programming/linkedlist (it was missing)
    for path in ['/', '/profile', '/contact', '/programming', '/programming/circle', 
                 '/programming/triangle', '/programming/linkedlist', '/programming/infix']:
        r = client.get(path)
        assert r.status_code == 200, f'{path} returned {r.status_code}'

def test_area_endpoints():
    client = app.test_client()
    r = client.post('/area/circle', data={'radius':'3'})
    assert r.status_code == 200
    assert 'Area of circle' in r.get_data(as_text=True)

    r = client.post('/area/triangle', data={'base':'4','height':'5'})
    assert r.status_code == 200
    assert 'Area of triangle' in r.get_data(as_text=True)

def test_infix_logic():
    # Test the logic directly
    assert infix_to_postfix("A + B") == "A B +"
    assert infix_to_postfix("A + B * C") == "A B C * +"
    assert infix_to_postfix("( A + B ) * C") == "A B + C *"
    assert infix_to_postfix("A + B + C") == "A B + C +" # Left associative
    # Test API
    client = app.test_client()
    r = client.post('/api/infix-to-postfix', json={'expression': 'A + B * C'})
    assert r.status_code == 200
    assert r.get_json()['postfix'] == "A B C * +"

if __name__ == '__main__':
    test_pages()
    test_area_endpoints()
    test_infix_logic()
    print('All tests passed')
