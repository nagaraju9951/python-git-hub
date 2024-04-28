# Import necessary modules
import pytest
from app import app

# Define test function
def test_hello_world():
    # Make a test client using Flask's test_client method
    client = app.test_client()

    # Use the client to make a request to the '/' route
    response = client.get('/')

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the response data contains the expected text
    assert b'Hello, World!' in response.data
