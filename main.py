# Desenvolvido por
# Lucas da Silva dos Santos
# Rafael Nascimento Lourenço

from AF import AF
from File_Utils import *
from AFNDE_to_AFND import AFNDE_to_AFND
from AFND_to_AFD import AFND_to_AFD


def get_line_content(line):
    try:
        return set(line[1:].strip().split(' '))
    except:
        raise ValueError(
            f'Erro ao tentar pegar os valores da linha do arquivo.')


def add_transictions_pattern(Q, A, T):
    try:
        for state in Q:
            for letter in A:
                if T.get(state) == None:
                    T[state] = {}
                T[state][letter] = set()

            T[state]['ê'] = set()
        return T
    except:
        raise ValueError(
            f'Erro ao tentar transformar o set de transicoes em um dicionario.')


def transform_transactions(aux_T, T):
    for transaction in aux_T:
        current_state = transaction[0]
        letter = transaction[1]
        next_state = transaction[2]
        T[current_state][letter].add(next_state)
    return T


if __name__ == "__main__":
    try:
        content_file = open_file('AFND_E_DEFINITION.txt').split('\n')

        # definicao para afnd-e
        # AF = (A, Q, q, T, F)
        A = []          # Alfabeto de entrada do automato
        Q = []          # Estados do automato
        F = []          # Estados finais do automato
        T = {}          # Funcao de transicao do automato
        aux_T = set()   # Auxiliar para construir o map de transicao
        q = None        # Estado inicial do automato

        P = []      # Palavras para testar

        line_count = 0
        for line in content_file:
            line_count += 1
            if line != '':
                match line[0]:
                    case 'A':
                        A = get_line_content(line)
                        if A == {''}:
                            raise ValueError(
                                f'Não foi possivel identificar o alfabeto de entrada na linha {line_count}.')
                    case 'Q':
                        Q = get_line_content(line)
                        if Q == {''}:
                            raise ValueError(
                                f'Não foi possivel identificar os estados na linha {line_count}.')
                    case 'q':
                        q = line[1:].strip()
                        if q == '':
                            raise ValueError(
                                f'Não foi possivel identificar o estado inicial na linha {line_count}.')
                    case 'F':
                        F = get_line_content(line)
                        if F == {''}:
                            raise ValueError(
                                f'Não foi possivel identificar o estado final na linha {line_count}.')
                    case 'T':
                        transaction = line[1:].strip().split()
                        try:
                            aux_T.add(
                                (transaction[0], transaction[1], transaction[2]))
                        except:
                            raise ValueError(
                                f'Não foi possivel identificar a transicao na linha {line_count}.')
                    case 'P':
                        word = line[1:].strip()
                        P.append(word)

        T = add_transictions_pattern(Q, A, T)
        T = transform_transactions(aux_T, T)

        M_AFNDE = AF(A, Q, q, T, F)
        M_AFND = AFNDE_to_AFND(M_AFNDE)
        M_AFD = AFND_to_AFD(M_AFND)

        for word in P:
            M_AFD.check_word(word)

        save_file("Words_results.txt", M_AFD.all_checks_str)

    except Exception as e:
        print("Ocorreu um erro.")
        print("Exceção: " + str(e))
