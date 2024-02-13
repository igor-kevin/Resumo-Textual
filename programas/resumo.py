# Programa para resumir um dado Texto passado na variável texto.
# Importando NLTK


import nltk
import string


# texto = '''A inteligência artificial (IA) é a capacidade de máquinas ou sistemas de realizar tarefas que normalmente exigiriam inteligência humana, como reconhecimento de voz, visão computacional, aprendizado de máquina, processamento de linguagem natural, tomada de decisão e resolução de problemas. A IA pode ser dividida em duas categorias principais: IA fraca e IA forte.

# A IA fraca, também chamada de IA estreita, é aquela que é projetada para executar uma tarefa específica, como jogar xadrez, traduzir idiomas ou dirigir carros. A IA fraca não tem consciência, entendimento ou raciocínio próprios, e depende de regras, algoritmos ou dados fornecidos por humanos. A maioria das aplicações de IA que existem hoje são exemplos de IA fraca, como assistentes virtuais, motores de busca, sistemas de recomendação, reconhecimento facial, etc.

# A IA forte, também chamada de IA geral, é aquela que é capaz de realizar qualquer tarefa intelectual que um humano pode fazer, como compreender, aprender, raciocinar, criar e se adaptar. A IA forte teria consciência, entendimento e raciocínio próprios, e não dependeria de regras, algoritmos ou dados fornecidos por humanos. A IA forte ainda é um objetivo distante para a ciência e a tecnologia, e envolve muitos desafios teóricos, técnicos e éticos.


def resumir_texto(texto):
    if texto.count('.') > 3:
        tamanho = int(round(texto.count('.')/3, 0))
    else:
        tamanho = 1

    sem_ponto = [
        caracter for caracter in texto if caracter not in string.punctuation]
    sem_ponto = ''.join(sem_ponto)

    processamento = (palavra for palavra in sem_ponto.split(' ')
                     if palavra.lower()
                     not in nltk.corpus.stopwords.words('portuguese'))

    # print(nltk.corpus.stopwords.words('portuguese'))
    # print(*processamento)

    frequencia = {}

    for palavra in processamento:
        if palavra not in frequencia:
            frequencia[palavra] = 1
        else:
            frequencia[palavra] += 1

    # print(frequencia)

    frequencia_maxima = max(frequencia.values())
    for palavra in frequencia.keys():
        frequencia[palavra] = frequencia[palavra]/frequencia_maxima

    tokens = nltk.sent_tokenize(texto)
    pontuacao_frase = {}
    for frase in tokens:
        for palavra in nltk.word_tokenize(frase.lower()):
            if palavra in frequencia.keys():
                if frase not in pontuacao_frase.keys():
                    pontuacao_frase[frase] = frequencia[palavra]
                else:
                    pontuacao_frase[frase] += frequencia[palavra]

    frases_ordem = sorted(
        pontuacao_frase, key=pontuacao_frase.get, reverse=True)
    # print(frases_ordem)
    resumo = ' '.join(frases_ordem[:tamanho])
    return resumo
