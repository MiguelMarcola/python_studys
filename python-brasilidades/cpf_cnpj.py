from validate_docbr import CPF, CNPJ


class Document:

    @staticmethod
    def create_doc(document):
        document = str(document)
        if(len(document) == 11):
            return DocCpf(document)
        elif(len(document) == 14):
            return DocCnpj(document)
        else:
            raise ValueError("Document is Invalid!")


class DocCpf:
    def __init__(self, document):
        if self.cpf_validator(document):
            self.cpf = document
        else:
            raise ValueError("Invalid is CPF!")

    def cpf_validator(self, document):
        validator_cpf = CPF()
        return validator_cpf.validate(document)

    def format_cpf(self):
        format_cpf = CPF()
        return format_cpf.mask(self.cpf)

    def __str__(self):
        return f"CPF -> {self.format_cpf()}"


class DocCnpj:
    def __init__(self, document):
        if self.cnpj_validator(document):
            self.cnpj = document
        else:
            raise ValueError("Invalid is CNPJ!")

    def cnpj_validator(self, document):
        validator_cnpj = CNPJ()
        return validator_cnpj.validate(document)

    def format_cnpj(self):
        format_cnpj = CNPJ()
        return format_cnpj.mask(self.cnpj)

    def __str__(self):
        return f"CNPJ -> {self.format_cnpj()}"
