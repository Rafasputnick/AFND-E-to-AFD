# Desenvolvido por
# Lucas da Silva dos Santos
# Rafael Nascimento Lourenço

from AF import AF
from File_Utils import *
from AFNDE_to_AFND import AFNDE_to_AFND
from AFND_to_AFD import AFND_to_AFD


def get_line_content(text):
    return set(line[1:].strip().split(' '))


if __name__ == "__main__":
    try:
        content_file = open_file('AFND_E_DEFINITION.txt').split('\n')

        # definicao para afnd-e
        # AF = (A, Q, q, T, F)
        A = []      # Alfabeto de entrada do automato
        Q = []      # Estados do automato
        F = []      # Estados finais do automato
        T = {}      # Funcao de transicao do automato
        q = None    # Estado inicial do automato

        P = []      # Palavras para testar
        for line in content_file:
            if line != '':
                match line[0]:
                    case 'A':
                        A = get_line_content(line)
                    case 'Q':
                        Q = get_line_content(line)
                        for state in Q:
                            for letter in A:
                                if T.get(state) == None:
                                    T[state] = {}
                                T[state][letter] = set()

                            T[state]['ê'] = set()

                    case 'q':
                        q = line[1:].strip()
                    case 'F':
                        F = get_line_content(line)
                    # TODO: deixar mais generico onde a ordem nao importa
                    case 'T':
                        transaction = line[1:].strip().split()
                        current_state = transaction[0]
                        letter = transaction[1]
                        next_state = transaction[2]
                        T[current_state][letter].add(next_state)
                    case 'P':
                        word = line[1:].strip()
                        P.append(word)
        M_AFNDE = AF(A, Q, q, T, F)
        M_AFND = AFNDE_to_AFND(M_AFNDE)
        M_AFD = AFND_to_AFD(M_AFND)

        for word in P:
            M_AFD.check_word(word)
    except:
        print("Ocorreu um erro desconhecido.")
