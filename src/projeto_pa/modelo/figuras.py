class Figura:
    """
    Representa uma figura geométrica do sistema.

    Esta classe serve como classe base para todas as figuras
    desenhadas na aplicação.

    Responsabilidade:
        Armazenar as propriedades comuns das figuras.

    @author Marcelo, Murilo
    @version 1.0
    @since 1.0
    """
    def __init__(self, cor_borda="black", preenchimento=""):
        self.cor_borda = cor_borda
        self.preenchimento = preenchimento

    def desenhar(self, canvas, tracejado=False):
        pass

    def atualizar(self, x, y):
        pass

    def incompleta(self):
        return False


class Linha(Figura):
    """
    Representa uma linha.

    Responsabilidade:
        Armazenar os pontos inicial e final e desenhar uma linha.

    @author Marcelo, Murilo
    @version 1.0
    @since 1.0
    """
    def __init__(self, x, y, cor, preenchimento):
        super().__init__(cor, preenchimento)
        self.x1 = x
        self.y1 = y
        self.x2 = x
        self.y2 = y

    def atualizar(self, x, y):
        self.x2 = x
        self.y2 = y

    def desenhar(self, canvas, tracejado=False):
        opcoes = {}
        if tracejado:
            opcoes["dash"] = (4, 2)

        canvas.create_line(
            self.x1,
            self.y1,
            self.x2,
            self.y2,
            fill=self.cor_borda,
            **opcoes
        )

    def incompleta(self):
        return self.x1 == self.x2 and self.y1 == self.y2


class Rabisco(Figura):
    """
    Representa um rabisco feito pelo usuário.

    Responsabilidade:
        Armazenar todos os pontos do rabisco.

    @author Marcelo, Murilo
    @version 1.0
    @since 1.0
    """
    def __init__(self, x, y, cor, preenchimento):
        super().__init__(cor, preenchimento)
        self.pontos = [(x, y)]

    def atualizar(self, x, y):
        self.pontos.append((x, y))

    def desenhar(self, canvas, tracejado=False):
        opcoes = {}
        if tracejado:
            opcoes["dash"] = (4, 2)

        canvas.create_line(
            self.pontos,
            fill=self.cor_borda,
            **opcoes
        )

    def incompleta(self):
        return len(self.pontos) <= 1


class Retangulo(Figura):
    """
    Representa um retângulo.

    Responsabilidade:
        Armazenar as coordenadas dos vértices e desenhar um retângulo.

    @author Marcelo, Murilo
    @version 1.0
    @since 1.0
    """
    def __init__(self, x, y, cor, preenchimento):
        super().__init__(cor, preenchimento)
        self.x1 = x
        self.y1 = y
        self.x2 = x
        self.y2 = y

    def atualizar(self, x, y):
        self.x2 = x
        self.y2 = y

    def desenhar(self, canvas, tracejado=False):
        opcoes = {
            "outline": self.cor_borda,
            "fill": self.preenchimento
        }

        if tracejado:
            opcoes["dash"] = (4, 2)

        canvas.create_rectangle(
            self.x1,
            self.y1,
            self.x2,
            self.y2,
            **opcoes
        )

    def incompleta(self):
        return self.x1 == self.x2 and self.y1 == self.y2


class Oval(Figura):
    """
    Representa uma elipse.

    Responsabilidade:
        Armazenar as coordenadas necessárias para desenhar um oval.

    @author Marcelo, Murilo
    @version 1.0
    @since 1.0
    """
    def __init__(self, x, y, cor, preenchimento):
        super().__init__(cor, preenchimento)
        self.x1 = x
        self.y1 = y
        self.x2 = x
        self.y2 = y

    def atualizar(self, x, y):
        """
        Atualiza a posição final da figura.

        @param x Nova coordenada x.
        @param y Nova coordenada y.
        @return None
        """
        self.x2 = x
        self.y2 = y

    def desenhar(self, canvas, tracejado=False):
        """
        Desenha a figura no canvas.

        @param canvas Canvas onde será desenhada.
        @param tracejado Indica se o desenho deve ser tracejado.
        @return None
        """
        opcoes = {
            "outline": self.cor_borda,
            "fill": self.preenchimento
        }

        if tracejado:
            opcoes["dash"] = (4, 2)

        canvas.create_oval(
            self.x1,
            self.y1,
            self.x2,
            self.y2,
            **opcoes
        )

    def incompleta(self):
        """
        Verifica se a figura foi desenhada completamente.

        @return True caso esteja incompleta; False caso contrário.
        """
        return self.x1 == self.x2 and self.y1 == self.y2


class Circulo(Figura):
    """
    Representa um círculo.

    Responsabilidade:
        Garantir que largura e altura sejam iguais durante o desenho.

    @author Marcelo, Murilo
    @version 1.0
    @since 1.0
    """
    def __init__(self, x, y, cor, preenchimento):
        """
        Cria uma nova linha.

        @param x Coordenada x inicial.
        @param y Coordenada y inicial.
        @param cor Cor da borda.
        @param preenchimento Cor de preenchimento.
        """
        super().__init__(cor, preenchimento)
        self.x1 = x
        self.y1 = y
        self.x2 = x
        self.y2 = y

    def atualizar(self, x, y):
        self.x2 = x
        self.y2 = y

    def desenhar(self, canvas, tracejado=False):
        lado = min(
            abs(self.x2 - self.x1),
            abs(self.y2 - self.y1)
        )

        x2 = self.x1 + lado if self.x2 >= self.x1 else self.x1 - lado
        y2 = self.y1 + lado if self.y2 >= self.y1 else self.y1 - lado

        opcoes = {
            "outline": self.cor_borda,
            "fill": self.preenchimento
        }

        if tracejado:
            opcoes["dash"] = (4, 2)

        canvas.create_oval(
            self.x1,
            self.y1,
            x2,
            y2,
            **opcoes
        )

    def incompleta(self):
        return self.x1 == self.x2 and self.y1 == self.y2


class Poligono(Figura):
    """
    Representa um polígono.

    Responsabilidade:
        Armazenar uma lista de pontos que compõem um polígono.

    @author Marcelo, Murilo
    @version 1.0
    @since 1.0
    """
    def __init__(self, pontos, cor, preenchimento):
        super().__init__(cor, preenchimento)
        self.pontos = pontos

    def desenhar(self, canvas, tracejado=False):
        opcoes = {
            "outline": self.cor_borda,
            "fill": self.preenchimento
        }

        if tracejado:
            opcoes["dash"] = (4, 2)

        canvas.create_polygon(
            self.pontos,
            **opcoes
        )

    def incompleta(self):
        return len(self.pontos) < 3