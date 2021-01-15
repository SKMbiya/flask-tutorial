from flaskr import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

# test whether the response return from the server is 'Hello World' for the hello world route
# if not return an error
def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'