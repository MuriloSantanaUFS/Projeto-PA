class Figura:
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

        canvas.create_oval(
            self.x1,
            self.y1,
            self.x2,
            self.y2,
            **opcoes
        )

    def incompleta(self):
        return self.x1 == self.x2 and self.y1 == self.y2


class Circulo(Figura):
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