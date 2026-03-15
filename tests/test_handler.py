import json
import os
import sys

# Ensure project root is on sys.path so 'src' can be imported
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from src import handler


def test_handler_returns_expected_response():
    # Arrange
    event = {"test": "value"}

    # Act
    response = handler.handler(event, None)

    # Assert basic HTTP shape
    assert response["statusCode"] == 200
    assert response["headers"]["Content-Type"] == "application/json"

    # Assert body content
    body = json.loads(response["body"])
    assert body["id"] == 1
    assert body["title"] == "Learn Python"
