from app import app

def test_pages():
    client = app.test_client()
    for path in ['/', '/profile', '/contact', '/programming']:
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

if __name__ == '__main__':
    test_pages()
    test_area_endpoints()
    print('All tests passed')
