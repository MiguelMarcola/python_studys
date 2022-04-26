from cpf_cnpj import Document

cpf = "16905495727"
cnpj = "24632774000101"

object_cpf = Document.create_doc(cpf)
object_cnpj = Document.create_doc(cnpj)

print(object_cpf)
print(object_cnpj)
