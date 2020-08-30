"""Módulo para calcular média aritmética de notas."""


def calcula_media():
    """Função não recebe parametros."""
    nota = None
    lista_notas = []
    while nota != 0.0:
        nota = float(input('Digite sua nota ou 0 (zero) para terminar: '))
        if nota != 0.0:
            lista_notas.append(nota)
        else:
            break
    quantidade = len(lista_notas)
    soma = sum(lista_notas)
    media = soma / quantidade
    print(f'Sua média é: {media}')


if __name__ == '__main__':
    calcula_media()
