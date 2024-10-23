from tests.conftest import client
from tests.endpoints.mocks import SUCCESS_RESPONSE_TEXT, SUCCESS_FILE_CONTENT, BAD_FILE_CONTENT, BAD_RESPONSE_TEXT


def test_success_post_method():
    """
    Test the POST method for store records on db.
    Returns: successfull message.
    """
    response = client.post(
        "api/v0.0.1/files/", files={"file": ("test.csv", SUCCESS_FILE_CONTENT, "text/csv")})

    assert response.text == SUCCESS_RESPONSE_TEXT
    assert response.status_code == 200

def test_error_post_method():
    """
    Test the POST method for a file with no valid fields or values.
    Returns: unsuccessful message message.
    """
    response = client.post(
        "api/v0.0.1/files/", files={"file": ("test.csv", BAD_FILE_CONTENT, "text/csv")})

    assert response.text == BAD_RESPONSE_TEXT
    assert response.status_code == 400
