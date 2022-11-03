from AF import AF
from copy import deepcopy

def depth_search_empty_transactions(state):
    if len(state.T['ê']) == 0:
        return state.T
    return

def AFNDE_to_AFND(AFNDE: AF):
    auxAFNDE =  deepcopy(AFNDE)
    # percorro pelos estados e nao pelo estado inicial e ir descobrindo
    # pq pensei no caso de uma funcao de transicao representado num grafo bipartido
    # se em ambos tiverem transicoes vazias ele nao vai retornar uma afnd (que nao deve ter esse tipo de transicao)
    transactions = auxAFNDE.T
    for state in auxAFNDE.Q:
        empty_transaction = transactions[state].pop('ê', None)
        if len(empty_transaction) > 0:
            aux = []
            for next_states in empty_transaction:
                pass

    return auxAFNDE