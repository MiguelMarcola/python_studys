from validate_docbr import CPF, CNPJ


class Doc:
    def __init__(self, document, type_document):
        self.validate_type(type_document)
        self.type_document = type_document
        document = str(document)
        if self.type_document == "cpf":
            if self.cpf_validator(document):
                self.cpf = document
            else:
                raise ValueError("Invalid is CPF!")
        elif self.type_document == "cnpj":
            if self.cnpj_validator(document):
                self.cnpj = document
            else:
                raise ValueError("Invalid is CNPJ!")

    def validate_type(self, type_document):
        if (type_document == "cpf" or type_document == "cnpj"):
            pass
        else:
            raise ValueError("Type is invalid!")

    def cpf_validator(self, document):
        if(len(document) == 11):
            validator_cpf = CPF()
            return validator_cpf.validate(document)
        else:
            return False

    def cnpj_validator(self, document):
        if(len(document) == 14):
            validator_cnpj = CNPJ()
            return validator_cnpj.validate(document)
        else:
            return False

    def format_cpf(self):
        format_cpf = CPF()
        return format_cpf.mask(self.cpf)

    def format_cnpj(self):
        format_cnpj = CNPJ()
        return format_cnpj.mask(self.cnpj)

    def __str__(self):
        if self.type_document == "cpf":
            response = f"CPF -> {self.format_cpf()}"
        elif self.type_document == "cnpj":
            response = f"CNPJ -> {self.format_cnpj()}"

        return response
