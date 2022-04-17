from main import app, call_validator
from unittest.mock import patch


def test_validate_route():
    """
    Tests if validate call is routed i.e. the endpoint is found
    """

    test_iban = app.test_client()
    response = test_iban.get('/iban/validate/IBAN_123')

    assert response.status_code == 200


@patch('main.json')
@patch('main.Validator.validate')
def test_validate(mock_validate, _):
    """
    Tests if the validator class's validate function is called
    """

    call_validator('IBAN_123')
    assert mock_validate.called == True
