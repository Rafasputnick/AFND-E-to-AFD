from AF import AF


class AFD(AF):
    def __init__(self, A: list, Q: list, q: str, T: list, F: list) -> None:
        super().__init__(A, Q, q, T, F)

    def check_word(self, word):
        transactions = self.T
        cur_state = self.q
        for symbol in word:
            if cur_state != None and transactions[cur_state].get(symbol) != None:
                cur_state = transactions[cur_state][symbol]
            else:
                cur_state = None
        if cur_state in self.F:
            print(f'M aceita a palavra <{word}>')
        else:
            print(f'M rejeita a palavra <{word}>')
