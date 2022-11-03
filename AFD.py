from AF import AF

class AFD(AF):
    def __init__(self) -> None:
        super().__init__()

    def check_word(self, word):
        print(f'M aceita a palavra <{word}>')