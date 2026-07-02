from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor
from figuras import *

# Quando mouse é pressionado
def iniciar_figura_nova(event): 
    global figura_nova
# =========================
# ALTERAÇÕES - MURILO
# Adição de retângulo, oval e círculo
# =========================
    tipo = tipo_figura_var.get()

    if tipo == 'Linha':
        figura_nova = Linha(event.x, event.y, cor_borda, cor_preenchimento)

    elif tipo == "Rabisco":
     figura_nova = Rabisco(event.x, event.y, cor_borda, cor_preenchimento)

    elif tipo == "Retangulo":
     figura_nova = Retangulo(event.x, event.y, cor_borda, cor_preenchimento)

    elif tipo == "Oval":
     figura_nova = Oval(event.x, event.y, cor_borda, cor_preenchimento)

    elif tipo == "Circulo":
     figura_nova = Circulo(event.x, event.y, cor_borda, cor_preenchimento)
        

# Quando mouse é movido com o botão pressionado
def atualizar_figura_nova(event):
    figura_nova.atualizar(event.x, event.y)

    desenhar_figuras()
    desenhar_figura_nova()
        

 
# Quando mouse é solto

def incluir_figura_nova(event):
    global figura_nova

    if not figura_nova.incompleta():
        figuras.append(figura_nova)

    figura_nova = None
    desenhar_figuras()
    

def desenhar(figura, tracejado=False):
    figura.desenhar(canvas, tracejado)

def desenhar_figuras():

    canvas.delete("all")

    for figura in figuras:
        desenhar(figura)
        
def desenhar_figura_nova():
    if figura_nova is not None:
        desenhar(figura_nova, tracejado=True)

def escolher_cor_borda():
    global cor_borda

    cor = askcolor(title="Escolha a cor da borda")

    if cor[1] is not None:
        cor_borda = cor[1]
        
def escolher_cor_preenchimento():
    global cor_preenchimento

    cor = askcolor(title="Escolha a cor do preenchimento")

    if cor[1] is not None:
        cor_preenchimento = cor[1]




#******* MAIN *******#

figuras = []       # Todas as figuras desenhadas
figura_nova = None # Figura que está sendo desenhada, mas ainda não foi incluída em figuras
cor_borda = "black" #define a borda padrão para preta
cor_preenchimento = "" #sem preenchimento por padrao

root = Tk()
root.title('Projeto PA - Editor Gráfico')
frame = Frame(root)

# Widgets arranjados com Layout grid dentro de frame
paddings = {'padx': 5, 'pady': 5} 

# label
label = ttk.Label(frame,  text='Escolha uma figura para desenhar:')
label.grid(column=0, row=0, sticky=W, **paddings)

# option menu
tipo_figura_var = StringVar(root) # Guarda o tipo de figura selecionado no option menu (linha ou rabisco)
option_menu = ttk.OptionMenu(frame, tipo_figura_var,
                             'Linha', 'Linha', 'Rabisco', 'Retangulo', 'Oval', 'Circulo')

botao_cor = ttk.Button( #botao para selecionar cor da borda
    frame,
    text="Cor da borda",
    command=escolher_cor_borda
)

botao_preenchimento = ttk.Button( #botao preenchimento
    frame,
    text="Preenchimento",
    command=escolher_cor_preenchimento
)

botao_preenchimento.grid(column=3, row=0, padx=5, pady=5)

botao_cor.grid(column=2, row=0, padx=5, pady=5)
# =========================
# - Atualização do OptionMenu com novos tipos de figura (feito por Murilo)
# =========================



option_menu.grid(column=1, row=0, sticky=W, **paddings)

# Área de desenho
canvas = Canvas(frame, bg='white', width=600, height=600)
canvas.grid(column=0, row=1, columnspan=2, sticky=W, **paddings)

frame.pack()

# Eventos de mouse associados ao canvas - com seus callbacks
canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)

root.mainloop()