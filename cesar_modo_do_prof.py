# Tomás Abril
# --Criptografia Cesar--

import sys
import getopt

#import unidecode

# ---
# 62 caracteres
# 0 à 61
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def criptografa(des, k, in_name, out_name):
    if des:
        k *= -1

    f_in = open(in_name, 'r', encoding='utf8')
    texto_com_acento = f_in.read()
    frase_mod = ""

    # pra tirar os acentos
    #texto_original = unidecode.unidecode(texto_com_acento)
    texto_original = texto_com_acento
    print("texto original")
    print(texto_com_acento)
    print("texto convertido para ASCII")
    print(texto_original)

    for i in range(len(texto_original)):
        # ---
        if texto_original[i] in alfabeto:
            posicao = alfabeto.index(texto_original[i])
            posicao += k
            posicao = posicao % len(alfabeto)
            frase_mod += alfabeto[posicao]
        # oytros caracteres permanecem
        else:
            frase_mod += texto_original[i]
    # salvando no arquivo de saida
    f_out = open(out_name, 'w')
    f_out.write(frase_mod)
    f_in.close()
    f_out.close()
    print("resultado")
    print(frase_mod)


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
                  + " -i :arquivo de entrada\n -o :arquivo de saida\n"
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
