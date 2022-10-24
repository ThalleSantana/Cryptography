from tqdm import tqdm
from time import sleep
letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
rot = 3
def cesar(palavra, escolha):
    cesartext = ''
    for count in palavra:
        c_index = letras.index(count)
        if escolha == "C":
            cesartext += letras[(c_index + rot) % len(letras)]
        else:
            cesartext += letras[(c_index - rot) % len(letras)]
    return cesartext

def vigenere(palavra, termo, escolha):
    vigeneretext = ''
    for count in range(len(palavra)):
        if palavra[count] != '':
            posicao_letra_frase = int(letras.index(palavra[count]))
            posicao_letra_chave = int(letras.index(termo[count]))
            if escolha == "C":
                vigeneretext += str(letras[(posicao_letra_frase + posicao_letra_chave) % len(letras)])
            else:
                vigeneretext += str(letras[(posicao_letra_frase - posicao_letra_chave) % len(letras)])
        else:
            vigeneretext = ''
    return vigeneretext

while True:
    textoFinal = ""
    op = input('Deseja Criptografar ou Descriptografar? [C/D] ').upper().strip()
    if op == "C" or op == "D":
        texto = ''.join(str(input('Digite o Texto: ')).upper().strip().split())
        chave = ''.join(str(input('Digite a Chave: ')).upper().strip().split())
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
            textoFinal = cesar(texto, op)
            textoFinal2 = vigenere(textoFinal, chaveFinal, op)
            for c in tqdm(range(10)):
                sleep(0.3)
            print(f'Frase final: {textoFinal2}')
            esc = str(input('Deseja continuar? [S/N] ')).upper().strip()
            if esc == "N":
                break
    else:
        print('Opção Invalida!!!')
