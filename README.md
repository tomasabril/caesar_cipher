# caesar_cipher
exercicio seguranca de sistemas


O cifrador de César

Atividade: Produzir uma implementação do cifrador de César. Ele deve funcionar da seguinte forma:

Para cifrar:

cesar -c -k 5 < texto-aberto.txt > texto-cifrado.txt

Para decifrar:

cesar -d -k 5 < texto-cifrado.txt > texto-aberto.txt

Opções:

    -c : cifrar
    -d : decifrar
    -k n : valor da chave a ser usada

A rotação de caracteres deve ser feita somente sobre os caracteres [A-Z,a-z,0-9]. Caracteres acentuados devem ser tratados sem acento.
