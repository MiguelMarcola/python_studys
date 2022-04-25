from validate_docbr import CPF


class Cpf:
    def __init__(self, document):
        documento = str(document)
        if self.cpf_validator(documento):
            self.cpf = documento
        else:
            raise ValueError("Invalid CPF!")

    def cpf_validator(self, document):
        if(len(document) == 11):
            validator_cpf = CPF()
            return validator_cpf.validate(document)
        else:
            return False

    def format_cpf(self):
        format_cpf = CPF()
        return format_cpf.mask(self.cpf)

    def __str__(self) -> str:
        return self.format_cpf()
