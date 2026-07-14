import pickle


class Desenho:
    """
    Representa um desenho composto por diversas figuras.

    Responsabilidade:
        Gerenciar as figuras desenhadas e realizar operações
        de persistência.

    @author Marcelo, Murilo
    @version 1.0
    @since 1.0
    """

    def __init__(self):
        """
        Inicializa um desenho vazio.
        """
        self.figuras = []

    def adicionar(self, figura):
        self.figuras.append(figura)

    def limpar(self):
        self.figuras.clear()

    def salvar(self, arquivo):
        """
        Salva o desenho em um arquivo.

        @param arquivo Caminho do arquivo.
        @throws OSError Caso ocorra erro na gravação.
        """
        print("Salvando desenho em arquivo:", arquivo)
        with open(arquivo, "wb") as f:
            pickle.dump(self.figuras, f)

    def abrir(self, arquivo):
        """
        Carrega um desenho de um arquivo.

        @param arquivo Caminho do arquivo.
        @throws OSError Caso ocorra erro na leitura.
        """
        print("Abrindo desenho do arquivo:", arquivo)
        with open(arquivo, "rb") as f:
            self.figuras = pickle.load(f)