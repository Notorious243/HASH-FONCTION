def hashage(message):
    # Initialisation de la variable pour stocker le hash
    hash_valeur = 0

    # Parcourir chaque caractère du message

    for caractere in message:
        # ajouter la valeur ASCII du Caractère au Hash
        hash_valeur += ord(caractere)

        # Appliquer une opération XOR ou toute autre opération que vous préférez
        hash_valeur ^= (hash_valeur << 5) + (hash_valeur >> 2)

    # Convertir le résultat en une autre représentation hexadecimale

    return hex(hash_valeur)


MESSAGE = input(" VEUILLEZ INTRODUIRE UNE INFORMATION : ")
print()
print(f"MESSAGE HASHER : {hashage(MESSAGE)}")
