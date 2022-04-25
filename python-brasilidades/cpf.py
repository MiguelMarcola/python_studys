class Cpf:
    def __init__(self, document):
        documento = str(document)
        if self.cpf_validator(documento):
            self.cpf = documento
        else:
            raise ValueError("Invalid CPF!")

    def cpf_validator(self, document):
        if(len(document) == 11):
            return True
        else:
            return False

    def format_cpf(self):
        format_cpf = self.cpf[:3] + "." + self.cpf[3:6] + \
            "." + self.cpf[6:9] + "-" + self.cpf[9:]
        return format_cpf

    def __str__(self) -> str:
        return self.format_cpf()
