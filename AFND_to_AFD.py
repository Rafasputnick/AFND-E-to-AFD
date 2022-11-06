from AF import AF
from AFD import AFD
from copy import deepcopy

# elimina todas transicoes ambiguas transformando em um automato deterministico
def AFND_to_AFD(AFNDE: AF):
    M_AFND = deepcopy(AFNDE)

    M_AFD = AFD(M_AFND.A, M_AFND.Q, M_AFND.q, M_AFND.T, M_AFND.F)
    return M_AFD
