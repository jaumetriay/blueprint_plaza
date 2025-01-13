
# pylint: disable=C0116
"""Test module for Blueprint Plaza routes."""

def test_404_error(client):
    response = client.get('/nonexistent-route')
    assert response.status_code == 404
    assert b'404.html' in response.data


def test_index_redirect(client):
    response = client.get('/')
    assert response.status_code == 302
    assert response.location.endswith('/home')


def test_home_route(client, mocker):
    mock_ads = [{'id': 1, 'title': 'Test Ad'}]
    mocker.patch('utils.read_json.load_ads', return_value=mock_ads)
    response = client.get('/home')
    assert response.status_code == 200
    assert b'Test Ad' in response.data


def test_get_ad_route(client, mocker):
    mock_ads = [{'id': 1, 'title': 'Test Ad'}]
    mocker.patch('utils.read_json.load_ads', return_value=mock_ads)
    response = client.get('/ad/1')
    assert response.status_code == 200
    assert b'Test Ad' in response.data


def test_get_nonexistent_ad(client, mocker):
    mock_ads = [{'id': 1, 'title': 'Test Ad'}]
    mocker.patch('utils.read_json.load_ads', return_value=mock_ads)
    response = client.get('/ad/999')
    assert response.status_code == 404


def test_cached_load_ads(app, mocker):
    with app.test_request_context():
        mock_load_ads = mocker.patch('utils.read_json.load_ads')
        mock_load_ads.return_value = [{'id': 1, 'title': 'Test Ad'}]

        # First call should hit the actual function
        app.view_functions['home']()
        assert mock_load_ads.call_count == 1

        # Second call should use cached result
        app.view_functions['home']()
        assert mock_load_ads.call_count == 1
