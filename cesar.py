
print("--Criptografia Cesar--\n")
frase_original = input("digite a frase a ser criptografada:\n").lower()

k = int(input("valor de k: "))


frase_mod = ""

for i in range(len(frase_original)):
    if 96 < ord(frase_original[i]) < 123 :
        num = ord(frase_original[i]) - 97 + k
        num = num%26
        num = num + 97
        frase_mod += chr(num)
    else:
        frase_mod += frase_original[i]



print("\nfrase criptografada:\n" + frase_mod)

