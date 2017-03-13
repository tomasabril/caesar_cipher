# Tomás Abril
# --Criptografia Cesar--

import sys
import getopt


# import unidecode

# ---

def criptografa(des, k, in_name, out_name):
    if des:
        k *= -1

    f_in = open(in_name, 'r')
    texto_original = f_in.read()
    frase_mod = ""

    # pra tirar os acentos
    #    texto_original = unidecode._unidecode(texto_original)

    for i in range(len(texto_original)):
        # numeros
        if 48 <= ord(texto_original[i]) <= 57:
            num = ord(texto_original[i]) - 48 + k
            num = num % 10
            num = num + 48
            frase_mod += chr(num)
        # letras minusculas
        elif 97 <= ord(texto_original[i]) <= 122:
            num = ord(texto_original[i]) - 97 + k
            num = num % 26
            num = num + 97
            frase_mod += chr(num)
        # letras MAIUSCULAS
        elif 65 <= ord(texto_original[i]) <= 90:
            num = ord(texto_original[i]) - 65 + k
            num = num % 26
            num = num + 65
            frase_mod += chr(num)
        # oytros caracteres permanecem
        else:
            frase_mod += texto_original[i]
        # salvando no arquivo de saida
        f_out = open(out_name, 'w')
        f_out.write(frase_mod)
        f_in.close()
        f_out.close()


def main(argv):
    k = 0
    desc = False
    try:
        opts, args = getopt.getopt(argv, "hcdk:i:o:")
    except getopt.GetoptError:
        print('erro ao interpretar comando\nmodo de uso:\ncesar.py -c -k 3 -i input.txt -o output.txt')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print("modo de uso:\ncesar.py -c -k 3 -i texto.txt -o saida.txt\nopcoes:\n"
                  + " -i :arquivo de entrada\n -o :arquivo de saida"
                  + " -c :criptografa\n -d :descriptografa\n -k n :valor da chave")
            sys.exit()
        elif opt in ("-i"):
            inputfile_name = arg
        elif opt in ("-o"):
            outputfile_name = arg
        elif opt in ("-c"):
            desc = False
        elif opt in ("-d"):
            desc = True
        elif opt in ("-k"):
            k = int(arg)

    criptografa(desc, k, inputfile_name, outputfile_name)


if __name__ == "__main__":
    main(sys.argv[1:])
