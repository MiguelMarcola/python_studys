import re


class Tel:
    def __init__(self, number):
        if self.validator_tel(number):
            self.number = number
        else:
            raise ValueError("Invalid Number!")

    def validator_tel(self, number):
        default = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
        response = re.search(default, number)
        if response:
            return True
        else:
            return False
