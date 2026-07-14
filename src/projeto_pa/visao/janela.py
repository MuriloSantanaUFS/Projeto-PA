from tkinter import *
from tkinter import ttk


class Janela:
    """
    Representa a interface gráfica do sistema.

    Responsabilidade:
        Criar todos os componentes visuais utilizados pela aplicação.

    @author Marcelo, Murilo
    @version 1.0
    @since 1.0
    """

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

        self.botao_salvar = ttk.Button(frame, text="Salvar")
        self.botao_salvar.grid(column=4, row=0, padx=5, pady=5)

        self.botao_abrir = ttk.Button(frame, text="Abrir")
        self.botao_abrir.grid(column=5, row=0, padx=5, pady=5)

        self.canvas = Canvas(frame, bg="white", width=600, height=600)
        self.canvas.grid(column=0, row=1, columnspan=6, sticky=W, **paddings)

        frame.pack()