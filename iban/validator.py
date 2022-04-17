import json
import re


class Validator:
    """
    Class containing functions to validate an IBAN
    """

    def __init__(self, iban: str) -> None:
        """
        Initializes the class object
        :param iban: IBAN in string format
        """

        self.iban = iban
        with open('config/iban_attributes.json', 'r') as file:
            self.iban_attributes = json.load(file)
    
    def validate(self) -> str:
        """
        Co-ordinates the various IBAN validatipn functions
        :return: string stating whether IBAN is valid
        """

        if self.country_code_exists():
            if self.check_length():
                if self.perform_mod_operation():
                    return f"Nice! IBAN: {self.iban} is valid"
        
        return f"Oops! IBAN: {self.iban} is invalid"
    
    def country_code_exists(self) -> bool:
        """
        Checks if the country code in the IBAN exists
        :return: True if country code exists else False
        """

        if self.iban[:2] in self.iban_attributes.keys():
            return True
        else:
            return False

    def check_length(self) -> bool:
        """
        Checks if IBAN is of valid length. Length is different for different countries.
        Here the length check is based on the country code present in the provided IBAN
        :return: True if lenght is valid else False
        """

        if len(self.iban) == self.iban_attributes.get(self.iban[:2]).get('length'):
            return True
        else:
            return False

    def perform_mod_operation(self) -> bool:
        """
        Manipulates IBAN string necessarily and performs mod operation on it.
        Here the check is based on ISO 7064, which states that if when the IBAN is divided by 97 and the
        resultant remainder is 1 then the IBAN can be considered valid
        :return: True if the remainder is 1 else False
        """

        rearranged_iban = self.iban[4:] + self.iban[:4]
        converted_iban = re.sub('[A-Z]', lambda m: str(ord(m.group()) - 55), rearranged_iban)

        if (int(converted_iban) % 97) == 1:
            return True
        else:
            return False




            


