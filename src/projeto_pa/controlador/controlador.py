from tkinter.colorchooser import askcolor
from modelo.figuras import Linha, Rabisco, Retangulo, Oval, Circulo

class Controlador:

    def __init__(self, desenho, janela):
        self.desenho = desenho
        self.janela = janela

        self.figura_nova = None
        self.cor_borda = "black"
        self.cor_preenchimento = ""

        self.janela.botao_cor.config(command=self.escolher_cor_borda)
        self.janela.botao_preenchimento.config(command=self.escolher_cor_preenchimento)

        self.janela.canvas.bind("<ButtonPress-1>", self.iniciar_figura_nova)
        self.janela.canvas.bind("<B1-Motion>", self.atualizar_figura_nova)
        self.janela.canvas.bind("<ButtonRelease-1>", self.incluir_figura_nova)

    def iniciar_figura_nova(self, event):

        tipo = self.janela.tipo_figura_var.get()

        if tipo == "Linha":
            self.figura_nova = Linha(event.x, event.y, self.cor_borda, self.cor_preenchimento)

        elif tipo == "Rabisco":
            self.figura_nova = Rabisco(event.x, event.y, self.cor_borda, self.cor_preenchimento)

        elif tipo == "Retangulo":
            self.figura_nova = Retangulo(event.x, event.y, self.cor_borda, self.cor_preenchimento)

        elif tipo == "Oval":
            self.figura_nova = Oval(event.x, event.y, self.cor_borda, self.cor_preenchimento)

        elif tipo == "Circulo":
            self.figura_nova = Circulo(event.x, event.y, self.cor_borda, self.cor_preenchimento)

    def atualizar_figura_nova(self, event):

        self.figura_nova.atualizar(event.x, event.y)

        self.desenhar_figuras()
        self.desenhar_figura_nova()

    def incluir_figura_nova(self, event):

        if not self.figura_nova.incompleta():
            self.desenho.adicionar(self.figura_nova)

        self.figura_nova = None
        self.desenhar_figuras()

    def desenhar(self, figura, tracejado=False):
        figura.desenhar(self.janela.canvas, tracejado)

    def desenhar_figuras(self):

        self.janela.canvas.delete("all")

        for figura in self.desenho.figuras:
            self.desenhar(figura)

    def desenhar_figura_nova(self):

        if self.figura_nova is not None:
            self.desenhar(self.figura_nova, tracejado=True)

    def escolher_cor_borda(self):

        cor = askcolor(title="Escolha a cor da borda")

        if cor[1] is not None:
            self.cor_borda = cor[1]

    def escolher_cor_preenchimento(self):

        cor = askcolor(title="Escolha a cor do preenchimento")

        if cor[1] is not None:
            self.cor_preenchimento = cor[1]