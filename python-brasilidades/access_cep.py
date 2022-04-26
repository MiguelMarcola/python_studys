import re
import requests


class SearchAddress:
    def __init__(self, cep):
        cep = str(cep)
        if (self.validator_cep(cep)):
            self.cep = cep
        else:
            raise ValueError("Invalid CEP!")

    def validator_cep(self, cep):
        if len(cep) != 8:
            return False
        default = "([0-9]{5})([0-9]{3})"
        response = re.search(default, cep)
        return response

    def mask_cpf(self):
        default = "([0-9]{5})([0-9]{3})"
        response = re.search(default, self.cep)
        mask_cpf = f"{response.group(1)}-{response.group(2)}"
        return mask_cpf

    def request_api(self):
        request = requests.get(f"https://viacep.com.br/ws/{self.cep}/json")
        response = request.text
        print(response)

    def __str__(self) -> str:
        return f"{self.mask_cpf()}"
