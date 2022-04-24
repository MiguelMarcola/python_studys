from unittest.case import _AssertRaisesContext


usarios_data_science = [15, 23, 43, 56]
usuarios_machine_learnig = [13, 23, 56, 42]

assistiram = []
assistiram.extend(usarios_data_science)
print(assistiram)


assistiram = usarios_data_science.copy()
assistiram.extend(usuarios_machine_learnig)
print(assistiram)


assitiram = set(assistiram)
print(assitiram)
print(set([15, 23, 43, 56]))


usarios_data_science = {15, 23, 43, 56}
usuarios_machine_learnig = {13, 23, 56, 42}


for usuario in set(assistiram):
    print(usuario)


print(usuarios_machine_learnig | usarios_data_science)


print(usuarios_machine_learnig & usarios_data_science)


print(usuarios_machine_learnig - usarios_data_science)
print(usarios_data_science - usuarios_machine_learnig)


print(usarios_data_science ^ usuarios_machine_learnig)
