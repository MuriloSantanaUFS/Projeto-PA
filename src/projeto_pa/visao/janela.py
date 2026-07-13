from tkinter import *
from tkinter import ttk


class Janela:

    def __init__(self):

        self.root = Tk()
        self.root.title("Projeto PA - Editor Gráfico")

        frame = Frame(self.root)

        paddings = {"padx": 5, "pady": 5}

        label = ttk.Label(frame, text="Escolha uma figura para desenhar:")
        label.grid(column=0, row=0, sticky=W, **paddings)

        self.tipo_figura_var = StringVar(self.root)

        option_menu = ttk.OptionMenu(
            frame,
            self.tipo_figura_var,
            "Linha",
            "Linha",
            "Rabisco",
            "Retangulo",
            "Oval",
            "Circulo"
        )

        option_menu.grid(column=1, row=0, sticky=W, **paddings)

        self.botao_cor = ttk.Button(frame, text="Cor da borda")
        self.botao_cor.grid(column=2, row=0, padx=5, pady=5)

        self.botao_preenchimento = ttk.Button(frame, text="Preenchimento")
        self.botao_preenchimento.grid(column=3, row=0, padx=5, pady=5)

        self.canvas = Canvas(frame, bg="white", width=600, height=600)
        self.canvas.grid(column=0, row=1, columnspan=4, sticky=W, **paddings)

        frame.pack()