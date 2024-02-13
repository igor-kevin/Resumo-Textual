import os


def muda_dir():
    pasta_dir = 'textos'
    os.chdir(pasta_dir)


def todos_arquivos():
    return os.listdir()


def retorna_texto(arquivo):
    with open(arquivo, 'r') as f:
        texto = f.read()
    return texto


def criar_novo_arquivo(arquivo, texto):
    novo_nome_temp = arquivo.split('.')
    novo_nome_temp.append('_resumo.')
    print(novo_nome_temp)
    print(novo_nome_temp[-3], '-3')
    novo_nome = novo_nome_temp[-3] + (novo_nome_temp[-1]) + 'txt'

    print('terminou xd', novo_nome)
    with open(novo_nome, 'w+') as f:
        print('entrei no texto e tal')
        f.write(texto)
        return True
    return False


if __name__ == '__main__':
    muda_dir()
    todos = todos_arquivos()
    for arquivo in todos:
        if arquivo.endswith('.txt'):
            print(retorna_texto(arquivo))
