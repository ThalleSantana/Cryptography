from tqdm import tqdm
from time import sleep
letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
while True:
    textoFinal = ""
    op = input('Deseja Criptografar ou Descriptografar? [C/D] ').upper().strip()
    if op == "C" or op == "D":
        texto = ''.join(str(input('Digite o Texto: ')).upper().strip().split())
        chave = str(input('Digite a Chave: ')).upper()
        chaveFinal = ""
        if len(chave) > len(texto):
            print('A chave é maior que a frase!!!')
        else:
            i = int(0)
            while len(chaveFinal) < len(texto):
                chaveFinal += chave[i]
                i += 1
                if i == len(chave):
                    i = 0
            for i in range(len(texto)):
                if texto[i] != ' ':
                    posicao_letra_frase = int(letras.index(texto[i]))
                    posicao_letra_chave = int(letras.index(chaveFinal[i]))
                    if op == "C":
                        textoFinal += str(letras[(posicao_letra_frase + posicao_letra_chave) % len(letras)])
                    else:
                        textoFinal += str(letras[(posicao_letra_frase - posicao_letra_chave) % len(letras)])
                else:
                    textoFinal = ' '
            for c in tqdm(range(10)):
                sleep(1)
            print(f'Frase final: {textoFinal}')
            esc = str(input('Deseja continuar? [S/N] ')).upper().strip()
            if esc == "N":
                break
    else:
        print('Opção Invalida!!!')
