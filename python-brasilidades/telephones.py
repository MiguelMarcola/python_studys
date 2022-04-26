import re


class Tel:
    def __init__(self, number):
        if self.validator_tel(number):
            self.number = number
        else:
            raise ValueError("Invalid Number!")

    def validator_tel(self, number):
        default = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        response = re.search(default, number)
        if response:
            return True
        else:
            return False

    def mask_number(self):
        default = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        response = re.search(default, self.number)
        if response.group(1):
            mask_number = f"+{response.group(1)}({response.group(2)}){response.group(3)}-{response.group(4)}"
        else:
            mask_number = f"+55({response.group(2)}){response.group(3)}-{response.group(4)}"
        return mask_number

    def __str__(self):
        return self.mask_number()
