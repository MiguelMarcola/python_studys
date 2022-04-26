from cpf_cnpj import Document
from dates import Dates
from telephones import Tel
from access_cep import SearchAddress

cpf = "74125434077"
cnpj = "54938235000158"

object_cpf = Document.create_doc(cpf)
object_cnpj = Document.create_doc(cnpj)

created = Dates()

phone = "24999041542"

phone_number = Tel(phone)


address = SearchAddress("01153000")

print(object_cpf)
print(object_cnpj)

print(created)

print(phone_number)

print(address)
