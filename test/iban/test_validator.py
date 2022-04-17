from iban.validator import Validator
from unittest.mock import patch


@patch('iban.validator.json')
@patch('iban.validator.open')
@patch('iban.validator.Validator.perform_mod_operation')
@patch('iban.validator.Validator.check_length')
@patch('iban.validator.Validator.country_code_exists')
def test_validate_valid_iban(mock_code_exists, mock_chk_len, mock_mod_op, *_):
    """
    Testing validate function response when a valid IBAN is provided
    """

    validator = Validator('IBAN_123')
    mock_code_exists.return_value = True
    mock_chk_len.return_value = True
    mock_mod_op.return_value = True

    response = validator.validate()
    assert response  == "Nice! IBAN: IBAN_123 is valid"


@patch('iban.validator.json')
@patch('iban.validator.open')
@patch('iban.validator.Validator.perform_mod_operation')
@patch('iban.validator.Validator.check_length')
@patch('iban.validator.Validator.country_code_exists')
def test_validate_invalid_iban(mock_code_exists, mock_chk_len, mock_mod_op, *_):
    """
    Testing validate function response when a invalid IBAN is provided
    """

    validator = Validator('IBAN_123')
    mock_code_exists.return_value = True
    mock_chk_len.return_value = True
    mock_mod_op.return_value = False

    response = validator.validate()
    assert response  == "Oops! IBAN: IBAN_123 is invalid"


@patch('iban.validator.json')
@patch('iban.validator.open')
def test_country_code_exists(*_):
    """
    Testing the country_code_exists function's response when IBAN's country code exists
    """

    validator = Validator('IBAN_123')
    validator.iban_attributes = {"IB": { "length": 24}}

    response = validator.country_code_exists()
    assert response == True


@patch('iban.validator.json')
@patch('iban.validator.open')
def test_country_code_not_exists(*_):
    """
    Testing the country_code_exists function's response when IBAN's country code doesn't exist
    """

    validator = Validator('IBAN_123')
    validator.iban_attributes = {"AD": { "length": 24}}

    response = validator.country_code_exists()
    assert response == False


@patch('iban.validator.json')
@patch('iban.validator.open')
def test_check_length_valid(*_):
    """
    Testing the check_length function's response when IBAN's length is valid
    """

    validator = Validator('IBAN_123')
    validator.iban_attributes = {"IB": { "length": 8}}

    response = validator.check_length()
    assert response == True


@patch('iban.validator.json')
@patch('iban.validator.open')
def test_check_length_invalid(*_):
    """
    Testing the check_length function's response when IBAN's length is invalid
    """

    validator = Validator('IBAN_123')
    validator.iban_attributes = {"IB": { "length": 9}}

    response = validator.check_length()
    assert response == False


@patch('iban.validator.json')
@patch('iban.validator.open')
def test_perform_mod_operation_valid(*_):
    """
    Testing the perform_mod_operation function's response when IBAN checksum is valid
    """

    validator = Validator('DO22ACAU00000000000123456789')

    response = validator.perform_mod_operation()
    assert response == True


@patch('iban.validator.json')
@patch('iban.validator.open')
def test_perform_mod_operation_invalid(*_):
    """
    Testing the perform_mod_operation function's response when IBAN checksum is invalid
    """

    validator = Validator('DO22ACAU00000000000123456780')

    response = validator.perform_mod_operation()
    assert response == False
