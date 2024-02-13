from resumo import resumir_texto
from manager import retorna_texto, todos_arquivos, muda_dir, criar_novo_arquivo

if __name__ == '__main__':
    muda_dir()
    arquivos = todos_arquivos()
    resumos = {}
    for arquivo in arquivos:
        if arquivo.endswith('.txt') and not arquivo.endswith('resumo.txt'):
            resumos[arquivo] = resumir_texto(retorna_texto(arquivo))
    print(resumos, 'AAAAAAAAA')
    for a, b in resumos.items():
        print('nome:', a)
        criar_novo_arquivo(a, b)
