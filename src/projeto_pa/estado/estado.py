from modelo.figuras import Linha, Rabisco, Retangulo, Oval, Circulo


class EstadoFerramenta:
    """
    Representa o estado da ferramenta de desenho selecionada pelo usuário.

    Responsabilidade:
        Definir a interface para criação da figura associada
        ao estado atual do controlador, evitando código condicional
        nos métodos do Controlador.

    @author Marcelo, Murilo
    @version 1.0
    @since 1.0
    """

    def criar_figura(self, x, y, cor_borda, cor_preenchimento):
        pass


class EstadoLinha(EstadoFerramenta):
    """
    Estado responsável por criar figuras do tipo Linha.

    @author Marcelo, Murilo
    @version 1.0
    @since 1.0
    """

    def criar_figura(self, x, y, cor_borda, cor_preenchimento):
        return Linha(x, y, cor_borda, cor_preenchimento)


class EstadoRabisco(EstadoFerramenta):
    """
    Estado responsável por criar figuras do tipo Rabisco.

    @author Marcelo, Murilo
    @version 1.0
    @since 1.0
    """

    def criar_figura(self, x, y, cor_borda, cor_preenchimento):
        return Rabisco(x, y, cor_borda, cor_preenchimento)


class EstadoRetangulo(EstadoFerramenta):
    """
    Estado responsável por criar figuras do tipo Retangulo.

    @author Marcelo, Murilo
    @version 1.0
    @since 1.0
    """

    def criar_figura(self, x, y, cor_borda, cor_preenchimento):
        return Retangulo(x, y, cor_borda, cor_preenchimento)


class EstadoOval(EstadoFerramenta):
    """
    Estado responsável por criar figuras do tipo Oval.

    @author Marcelo, Murilo
    @version 1.0
    @since 1.0
    """

    def criar_figura(self, x, y, cor_borda, cor_preenchimento):
        return Oval(x, y, cor_borda, cor_preenchimento)


class EstadoCirculo(EstadoFerramenta):
    """
    Estado responsável por criar figuras do tipo Circulo.

    @author Marcelo, Murilo
    @version 1.0
    @since 1.0
    """

    def criar_figura(self, x, y, cor_borda, cor_preenchimento):
        return Circulo(x, y, cor_borda, cor_preenchimento)